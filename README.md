# Financial News and Short-Horizon Market Reactions: FinBERT Based NLP Transformers for Normalized Prices and Volatility
*by Yifei Fu, Zhonghao Liu, and Shilun Dai from Columbia University*

Text models are increasingly deployed in financial markets, including ultra-low- latency systems where news feeds can trigger trades at millisecond timescales. In this project we ask a simpler but fundamental question: given realistic minute-level news and price data, how well can a pretrained financial language model, FinBERT, predict short-horizon market reactions when labels are carefully normalized by option-implied volatility?

We build a dataset of news for the 50 largest U.S. equities by market capitaliza- tion (S&P 500 constituents), aligned to 1–60 minute post-news returns and 5–60 minute realized volatility, and scale both by previous-day 30-day at-the-money (ATM) implied volatility using either an approximate straddle price (for price movements) or direct IV normalization (for volatility). Our first stage evaluates a head-only FinBERT classifier on straddle-normalized price movements across multiple horizons and label granularities (2/3/7-class). Despite clear improvements over a zero-shot FinBERT sentiment baseline, normalized price moves remain very hard to predict, with accuracies only modestly above chance. Motivated by the fact that signed returns at minute horizons are driven by many non-text factors, we shift to IV-normalized realized volatility and add a lightweight LoRA adapter on top of FinBERT. On these volatility tasks, LoRA-tuned FinBERT delivers consistent and non-trivial gains over the zero-shot baseline (e.g., roughly +10 percentage points for 30-minute 2-class volatility), suggesting that IV-normalized volatility is a more stable and learnable signal of “how much” the market reacts to news than the signed return itself.

You can read our report at `financial_news_and_short_horizon_market_reactions.pdf`.

---

`nlp_stock_price_movement_prediction` includes everything to build our fine-tuned transformer for real data predictions. `dummy_analysis_finbert_no_ticker.ipynb` is a prototype we used to analyze the attention mechanism of processing financial news.
