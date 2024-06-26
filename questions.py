# questions.py

life_stage_questions = [
    {
        "question": "What is your current age?",
        "answers": [
            {"answer": "60 or older", "score": 1},
            {"answer": "50 to 59", "score": 2},
            {"answer": "40 to 49", "score": 3},
            {"answer": "30 to 39", "score": 4},
            {"answer": "20 to 29", "score": 5},
        ]
    },
    {
        "question": "When do you expect to need to withdraw cash from your investment portfolio?",
        "answers": [
            {"answer": "Less than 1 year", "score": 1},
            {"answer": "1 to 2 years", "score": 2},
            {"answer": "2 to 5 years", "score": 3},
            {"answer": "5 to 10 years", "score": 4},
            {"answer": "Not for at least 10 years", "score": 5},
        ]
    },
    {
        "question": "Which best describes you?",
        "answers": [
            {"answer": "Young family with a home. Mortgage and childcare costs, maintaining only small cash balances.", "score": 1},
            {"answer": "Retired. Rely on existing funds and investments to maintain lifestyle in retirement.", "score": 2},
            {"answer": "Mature family. In peak earning years, mortgage under control. Ready to start planning for retirement.", "score": 3},
            {"answer": "Preparing for retirement. Own home and few financial burdens.", "score": 4},
            {"answer": "Single with few financial burdens.", "score": 5},
        ]
    }
]

financial_resources_questions = [
    {
        "question": "How many months of current living expenses could you cover with your present savings and liquid, short-term investments, before you would have to draw on your investment portfolio?",
        "answers": [
            {"answer": "Less than 3 months.", "score": 1},
            {"answer": "3 to 6 months.", "score": 2},
            {"answer": "6 to 12 months.", "score": 3},
            {"answer": "More than 12 months.", "score": 4},
        ]
    },
    {
        "question": "Over the next few years, what do you expect will happen to your income?",
        "answers": [
            {"answer": "It will probably decrease substantially", "score": 1},
            {"answer": "It will probably decrease slightly", "score": 2},
            {"answer": "It will probably stay the same", "score": 3},
            {"answer": "It will probably increase slightly", "score": 4},
            {"answer": "It will probably increase substantially", "score": 5},
        ]
    },
    {
        "question": "What percentage of your gross annual income have you been able to save in recent years?",
        "answers": [
            {"answer": "None", "score": 1},
            {"answer": "1 to 5%", "score": 2},
            {"answer": "5 to 10%", "score": 3},
            {"answer": "10 to 15%", "score": 4},
            {"answer": "more than 15%", "score": 5},
        ]
    },
    {
        "question": "Over the next few years, what do you expect will happen to your rate of savings?",
        "answers": [
            {"answer": "It will probably decrease substantially", "score": 1},
            {"answer": "It will probably decrease slightly", "score": 2},
            {"answer": "It will probably stay the same", "score": 3},
            {"answer": "It will probably increase slightly", "score": 4},
            {"answer": "It will probably increase substantially", "score": 5},
        ]
    }
]

investment_experience_questions = [
    {
        "question": "How familiar are you with investment matters?",
        "answers": [
            {"answer": "Not familiar at all and feel uncomfortable with the complexity.", "score": 1},
            {"answer": "Not very familiar when it comes to investments.", "score": 2},
            {"answer": "Somewhat familiar, I don’t fully understand investments.", "score": 3},
            {"answer": "Fairly familiar. I understand the various factors which influence investment performance.", "score": 4},
            {"answer": "Very familiar. I use research and other investment information to make investment decisions.", "score": 5},
        ]
    },
    {
        "question": "How long have you been investing, not counting your home or bank type deposits?",
        "answers": [
            {"answer": "This is my/our first investment.", "score": 1},
            {"answer": "Less than 3 years.", "score": 2},
            {"answer": "3 to 5 years.", "score": 3},
            {"answer": "6 to 10 years.", "score": 4},
            {"answer": "10+ years.", "score": 5},
        ]
    }
]

emotional_risk_tolerance_questions = [
    {
        "question": "What are your return expectations for your portfolio?",
        "answers": [
            {"answer": "I don’t care if my portfolio keeps pace with inflation; I just want to preserve my capital", "score": 1},
            {"answer": "My return should keep pace with inflation, with minimum volatility.", "score": 2},
            {"answer": "My return should be slightly more than inflation, with only moderate volatility.", "score": 3},
            {"answer": "My return should significantly exceed inflation, even if this could mean significant volatility.", "score": 4},
        ]
    },
    {
        "question": "How would you characterize your personality?",
        "answers": [
            {"answer": "I’m a pessimist. I always expect the worst.", "score": 1},
            {"answer": "I’m anxious. No matter what you say, I’ll worry.", "score": 2},
            {"answer": "I’m cautious but open to new ideas. Convince me.", "score": 3},
            {"answer": "I’m objective. Show me the pros and cons and I can make decisions and live with it.", "score": 4},
            {"answer": "I’m optimistic. Things always work out in the end.", "score": 5},
        ]
    },
    {
        "question": "Which would you prefer?",
        "answers": [
            {"answer": "Lower returns with negligible swings in portfolio value", "score": 1},
            {"answer": "Slightly higher returns with small swings in portfolio value", "score": 2},
            {"answer": "Moderate returns with moderate swings in portfolio value", "score": 3},
            {"answer": "Large returns annually with negative returns once in 6 years", "score": 4},
            {"answer": "Even higher returns annually with negative returns once in 3 years", "score": 5},
        ]
    },
    {
        "question": "When monitoring your investments over time, what do you think you will tend to focus on?",
        "answers": [
            {"answer": "Individual investments that are doing poorly.", "score": 1},
            {"answer": "Individual investments that are doing very well.", "score": 2},
            {"answer": "The recent results of my overall portfolio.", "score": 3},
            {"answer": "The long-term performance of my overall portfolio.", "score": 4},
        ]
    },
    {
        "question": "Suppose you had N10,000,000 to invest and the choice of 5 different portfolios with a range of possible outcomes after a single year. Which of the following portfolios would you feel most comfortable investing in?",
        "answers": [
            {"answer": "Portfolio A, which could have a balance ranging from N9,900,000 to N10,300,000 at the end of the year.", "score": 1},
            {"answer": "Portfolio B, which could have a balance ranging from N9,800,000 to N10,600,000 at the end of the year.", "score": 2},
            {"answer": "Portfolio C, which could have a balance ranging from N9,600,000 to N11,000,000 at the end of the year.", "score": 3},
            {"answer": "Portfolio D, which could have a balance ranging from N9,200,000 to N12,200,000 at the end of the year.", "score": 4},
            {"answer": "Portfolio E, which could have a balance ranging from N8,400,000 to N14,000,000 at the end of the year.", "score": 5},
        ]
    },
    {
        "question": "Which statement best describes your investment goals?",
        "answers": [
            {"answer": "Protect the value of my portfolio. In order to minimize the chance for loss, I am willing to accept the lower long-term returns provided by conservative investments.", "score": 1},
            {"answer": "Keep risk to a minimum while trying to achieve slightly higher returns than the returns provided by investments that are more conservative.", "score": 2},
            {"answer": "Balance moderate levels of risk with moderate levels of returns.", "score": 3},
            {"answer": "Maximize long-term investment returns. I am willing to accept large and sometimes dramatic short-term fluctuations in the value of this portfolio.", "score": 4},
        ]
    },
    {
        "question": "If the value of your investment portfolio dropped by 20% in one year, what would you do?",
        "answers": [
            {"answer": "Fire my investment advisor.", "score": 1},
            {"answer": "Move my money to more conservative investments immediately to reduce the potential for future losses.", "score": 2},
            {"answer": "Monitor the situation, and if it looks like things could continue to deteriorate, move some of my money to more conservative investments.", "score": 3},
            {"answer": "Consult with my investment advisor to ensure that my asset allocation is correct, and then ride it out.", "score": 4},
            {"answer": "Consider investing more because prices are so low.", "score": 5},
        ]
    },
    {
        "question": "Which portfolio would you feel most comfortable investing in?",
        "answers": [
            {"answer": "Portfolio A : returns 6% annually with no negative returns", "score": 1},
            {"answer": "Portfolio B : Returns 10% annually with negative returns once in 10 years", "score": 2},
            {"answer": "Portfolio C : Returns 15% with negative returns once in 7 years", "score": 3},
            {"answer": "Portfolio D : 20% annually with negative returns once in 5 years", "score": 4},
            {"answer": "Portfolio E : 25% returns annually with negative returns once in 3 years", "score": 5},
        ]
    },
    {
        "question": "Do you trade investments on a regular basis?",
        "answers": [
            {"answer": "No, I normally hold investments for more than 5 years", "score": 1},
            {"answer": "No, I normally hold investments for more than 1 year", "score": 2},
            {"answer": "Yes, More than once every six months", "score": 3},
            {"answer": "Yes, More than once a month", "score": 4},
            {"answer": "Yes, more than 30 times a year", "score": 5},
        ]
    },
    {
        "question": "Which of the following risks or events do you fear most?",
        "answers": [
            {"answer": "A loss of principal over any period of 1 year or less.", "score": 1},
            {"answer": "A rate of inflation that exceeds my rate of return over the long term, because it will erode the purchasing power of my money.", "score": 2},
            {"answer": "Portfolio performance that is insufficient to meet my goals.", "score": 3},
            {"answer": "Portfolio performance that is consistently less than industry benchmarks.", "score": 4},
            {"answer": "A missed investment opportunity that could have yielded higher returns over the long term, even though it entailed higher risk.", "score": 5},
        ]
    }
]