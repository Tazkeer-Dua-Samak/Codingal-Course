CREATE TABLE IF NOT EXISTS HACKER_NEWS (
    ARTICLE_ID INTEGER PRIMARY KEY,
    TITLE TEXT,
    URL TEXT,
    RATING TEXT
);

INSERT INTO HACKER_NEWS (ARTICLE_ID, TITLE, URL, RATING)
VALUES
(0001, 'OpenAI Launches GPT-5 with Human-Level Reasoning', 'https://news.openai.com/gpt5', 'five stars'),
(0002, 'Hackers Breach Major Cloud Platform', 'https://securitytoday.fake/hack-news', 'three stars'),
(0003, 'Scientists Discover Water on Mars Again', 'https://spaceupdates.fake/mars2025', 'four stars'),
(0004, 'New iPhone Model Breaks Sales Records', 'https://techbuzz.fake/iphone15', 'five stars'),
(0005, 'Local Startup Raises $10 Million in Funding', 'https://finance.fake/startup2025', 'four stars'),
(0006, 'Government Proposes New Data Privacy Laws', 'https://policy.fake/privacybill', 'three stars'),
(0007, 'Quantum Computing Breakthrough Achieved', 'https://science.fake/quantumleap', 'five stars'),
(0008, 'AI-Powered Cars Dominate the Market', 'https://auto.fake/aicars', 'four stars'),
(0009, 'Major Social Media Outage Frustrates Millions', 'https://technews.fake/outage', 'two stars'),
(0010, 'New Renewable Energy Source Discovered', 'https://greenenergy.fake/newtech', 'five stars');

SELECT * FROM HACKER_NEWS; 
SELECT * FROM HACKER_NEWS
WHERE RATING = 'five stars';
