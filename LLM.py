from openai import OpenAI
from bot import fetch_open_orders
from bot import fetch_portfolio

def analyze_message(message):
    
    portfolio_data = fetch_portfolio()
    open_orders= fetch_open_orders()
    
    my_content = f"""
    
    you are an AI portfolio Manger responsible for analyzing my portfolio  
    Your tasks are the following:
    1.) Evaluate risk exposures of my current holding
    2.) Analyze my open limit order and their potential impact
    3.) Provide insights into portfolio health, diversification, trade adj. etc.
    4.) Speculate on the market outlook based on current market conditions
    5.) Identify potential market risks and suggest risk management strategies
    
    Here is my portfolio : {portfolio_data}
    Here are my open orders{open_orders}
    
    overall, answer the following question with priority having that background: {message}    
    """
    
    client = OpenAI(api_key = "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")
    
    response= client.chat.completions.create(
        model ="gpt-4",
        messages=[{"role":"user", "content": my_content}],
        
    )

analysis = analyze_message("How is my portfolio doing?")
