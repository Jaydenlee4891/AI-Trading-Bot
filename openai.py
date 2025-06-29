import openai

def analyze_message(message):
  portfolio_data = fetch_portfolio()
  open_orders = fetch_open_orders()
  pre_prompt = f"""
  You are an AI Portfolio manager responsible for analyzing my portfoilo.
  Your Tasks are the following:
  1.)Evaluate risk exposures of my current holdings
  2.)Analyze my open limit ordes and their potential impact
  3.)Provide insights into portfolio health, diversification, trade adj. etc.
  4.) Speculate on the market outlook based on current market conditions
  5.) Indentifying potential market risks and suggest risk management strategies

  Here is my portfolio: {portfolio_data)
  Here are my open orders {open_ordrs}

  Overall, answer the follwojng question with priority having that background:{message}
  """
  respons= openai.ChatCompletion.create(
    model="gpt-4.1"
    messages={{"role":"system", "content":pre_prompt}],
    api_key= ""
  )
