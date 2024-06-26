from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from models.models import db, Portfolio, PortfolioInvestment

portfolio = Blueprint('portfolio', __name__)

@portfolio.route('/portfolio', methods=['GET'])
@login_required
def get_portfolio():
    user_portfolio = Portfolio.query.filter_by(user_id=current_user.id).first()
    if not user_portfolio:
        return jsonify({'error': 'Portfolio not found'}), 404

    investments = PortfolioInvestment.query.filter_by(portfolio_id=user_portfolio.id).all()
    investment_list = [
        {'investment_id': inv.investment_id, 'quantity': inv.quantity, 'current_value': inv.current_value}
        for inv in investments
    ]
    return jsonify({'portfolio_id': user_portfolio.id, 'total_value': user_portfolio.total_value, 'investments': investment_list})

@portfolio.route('/portfolio', methods=['POST'])
@login_required
def add_investment():
    data = request.get_json()
    investment_id = data['investment_id']
    quantity = data['quantity']
    current_value = data['current_value']

    user_portfolio = Portfolio.query.filter_by(user_id=current_user.id).first()
    if not user_portfolio:
        user_portfolio = Portfolio(user_id=current_user.id)
        db.session.add(user_portfolio)
        db.session.commit()

    portfolio_investment = PortfolioInvestment(
        portfolio_id=user_portfolio.id,
        investment_id=investment_id,
        quantity=quantity,
        current_value=current_value
    )
    db.session.add(portfolio_investment)
    db.session.commit()

    user_portfolio.total_value += current_value * quantity
    db.session.commit()

    return jsonify({'message': 'Investment added to portfolio successfully'})

@portfolio.route('/portfolio', methods=['PUT'])
@login_required
def update_investment():
    data = request.get_json()
    investment_id = data['investment_id']
    quantity = data['quantity']
    current_value = data['current_value']

    user_portfolio = Portfolio.query.filter_by(user_id=current_user.id).first()
    if not user_portfolio:
        return jsonify({'error': 'Portfolio not found'}), 404

    portfolio_investment = PortfolioInvestment.query.filter_by(portfolio_id=user_portfolio.id, investment_id=investment_id).first()
    if not portfolio_investment:
        return jsonify({'error': 'Investment not found in portfolio'}), 404

    user_portfolio.total_value -= portfolio_investment.current_value * portfolio_investment.quantity
    portfolio_investment.quantity = quantity
    portfolio_investment.current_value = current_value
    user_portfolio.total_value += current_value * quantity
    db.session.commit()

    return jsonify({'message': 'Investment updated successfully'})

@portfolio.route('/portfolio', methods=['DELETE'])
@login_required
def delete_investment():
    data = request.get_json()
    investment_id = data['investment_id']

    user_portfolio = Portfolio.query.filter_by(user_id=current_user.id).first()
    if not user_portfolio:
        return jsonify({'error': 'Portfolio not found'}), 404

    portfolio_investment = PortfolioInvestment.query.filter_by(portfolio_id=user_portfolio.id, investment_id=investment_id).first()
    if not portfolio_investment:
        return jsonify({'error': 'Investment not found in portfolio'}), 404

    user_portfolio.total_value -= portfolio_investment.current_value * portfolio_investment.quantity
    db.session.delete(portfolio_investment)
    db.session.commit()

    return jsonify({'message': 'Investment removed from portfolio successfully'})