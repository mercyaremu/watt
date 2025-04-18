# **👋Welcome**

Step softly, brave wanderer. You're just beginning to explore Solana’s first universal staking account.  
We are excited to have you here on the journey into the world of decentralized finance and liquid-staked tokens. Watt Protocol is the first universal staking account on Solana that generates real yield for users by capitalizing on natural market arbitrage opportunities, while also providing liquidity for other projects in the ecosystem.

Whether you are a seasoned DeFi enthusiast or just starting to dip your toes into the crypto waters, Watt Protocol offers a reimagined way to generating yield on Solana in a permissionless and trustless way. In this guide, we will walk you through everything you need to know about Watt Protocol, from its core concepts to practical usage. Let's dive into the electrifying world together\!

### **Save energy \- take shortcuts from here:**

**![Cover][image1]**  
[**Protocol walkthrough**](https://docs.watt.si/protocol-overview/liquid-staking-for-tokens)  
[Jump straight into basic concepts behind Watt](https://docs.watt.si/protocol-overview/liquid-staking-for-tokens)  
[![Cover][image2]](https://docs.watt.si/protocol-overview/liquid-staking-for-tokens)  
[**Manifesto**](https://docs.watt.si/manifesto)  
[Why are we building?](https://docs.watt.si/manifesto)  
[![Cover][image3]](https://docs.watt.si/manifesto)  
[**Ready to engage?**](https://docs.watt.si/contribution)  
[Everyone can participate in our moon mission](https://docs.watt.si/contribution)

# **Manifesto**

Deep beliefs impact products the most.  
Freedom to choose your financial products and retain your data plays a key role in our vision of the future. We believe that the advanced technology of blockchain will help make important parts of our decisions trustless and permissionless. In a world where plenty of centralized entities still decide on your access to capital and basic financial services, it is of vital importance to have products that only require an internet connection to use them.

Our vision is to bring democratized access to capital to as many people as possible. For this reason, we decided to utilize distributed ledger technology. Solana became our home, our basic infrastructure for building, while keeping a great user experience constantly in mind as an essential ingredient for our products.

# **Contribution**

Each stage of development opens new challenges for us and new options for you to participate and contribute.  
Right now, the best way is to get in touch with us, follow and vibe on:   
**X:** [https://x.com/wattprotocol](https://x.com/wattprotocol)

**Discord:** [https://discord.gg/cChe5CwQrh](https://discord.gg/cChe5CwQrh)

* [💥](https://docs.watt.si/protocol-overview)  
* [Protocol overview](https://docs.watt.si/protocol-overview)

# **Liquid staking for tokens**

Why hold just another idle token in your wallet when you can hold a liquid-staked token and earn yield along the way?  
**Liquid staking** is a mechanism that allows users to stake crypto assets while simultaneously receiving liquid token representations of their staked assets. These liquid-staked tokens can be freely traded, utilized in yield-generating strategies, or used as collateral within the broader DeFi ecosystem, effectively combining the benefits of staking rewards and liquidity.

Watt Protocol introduces the first liquid-staking service for Solana tokens. Any token can be wrapped into its liquid-staked representation, enabling users to simply **wrap, hold, and earn yield**.

Moreover, since liquid-staked Watt tokens are **fully composable**, they create new possibilities for product design, allowing other protocols and applications on Solana to freely integrate and take advantage of the intrinsic yield of Watt tokens.  
![][image4]

# **Volatility farming**

Imagine a world where the ups and downs of cryptocurrency prices aren't just a rollercoaster ride for investors, but actually a way to earn rewards. This is the essence of volatility farming.

### **What is a volatility farming?**

At its core, volatility farming is a way to make your **Solana liquid-staked tokens work for you** by taking advantage of the natural price swings in the market. In traditional finance, volatility is often seen as something to be wary of. But we turned this volatility into an opportunity \- users earn rewards regardless of whether prices are going up or down. It's not about predicting the market; it's about being part of the action.  
![][image5]

### **Why is volatility farming important for users?**

* **Sustainable source of yield**: Volatility farming provides a new way to earn yields that is not dependent on traditional methods like dilutive staking or lending, helping users in the ecosystem diversify their DeFi strategies.  
* **Market-neutral strategy**: Unlike traditional directional speculations where users profit only when prices go up, or short-selling when prices go down, volatility farming can provide returns regardless of market direction.  
* **Flexibility**: Users can enter or exit their positions at any time without long lock-up periods, offering greater liquidity and control over their assets.

The backbone of the protocol comprises of Watt assets, liquidity pools and fee distribution.

# **Arbitrage opportunities**

Volatility farming works ideally in environments characterized by **rapidly changing asset prices**, a scenario common in crypto markets. The supply side of volatility farming consists primarily of arbitrageurs and traders who actively pursue opportunities arising from price discrepancies between similar assets.

The Watt protocol satisfies **all fundamental conditions** essential for successful arbitrage:

* Watt tokens are freely tradable without requiring permission or encountering any constraints.  
* Watt tokens can always be redeemed back into their original underlying tokens.  
* Integration with permissionless decentralized exchanges (DEXs) makes opportunities accessible to everyone.

### **Examples of arbitrage trades in Watt protocol**

* **Scenario 1:** Suppose the wattBONK token trades at a lower price than the original BONK token. Arbitrageurs can capitalize on this price difference by buying wattBONK on a DEX and then unwrapping it into the native BONK token. The native BONK can subsequently be sold, completing the arbitrage. This opportunity persists until the price difference between wattBONK and BONK equals the sum of the transfer and unwrap fees associated with wattBONK.  
* **Scenario 2:** Conversely, if wattBONK trades at a higher price than the original BONK token, traders can take advantage of this situation by purchasing BONK tokens and wrapping them into wattBONK. The resulting liquid-staked wattBONK can then be sold on a DEX to complete the arbitrage. This arbitrage opportunity remains viable until the price difference between wattBONK and BONK matches the total wrap and transfer fees for wattBONK.

# **Volatility farming flywheel**

Let's dig deeper.  
Each component of the volatility farming flywheel can be further broken down to illustrate the internal workings of the protocol. Note that the term 'Watt asset' here refers to any Solana token wrapped as a liquid-staked token.  
![][image6]

# **Watt assets**

Watt assets are a **new type of tokenized asset** within the Solana ecosystem, developed as part of the Watt protocol. These assets are designed to capitalize on market volatility and provide new yield opportunities for token holders, liquidity providers, and arbitrageurs.

Watt assets are wrapped versions of existing tokens on Solana. When a user wraps a token using the Watt protocol, they receive a corresponding *wattToken* (e.g. BONK becomes *wattBONK*) \- a liquid-staked token. These *watt assets* represent **ownership of the underlying asset** while enabling additional functionality and intrinsic yield generation.

Watt assets:

* accrue value over time due to the protocol's fee structure  
* are backed with the underlying asset  
* are fully redeemable at any time  
* do not require you to actively claim yield, similar to how liquid-staked SOL operates  
* can be tax-effective — the yield is realized when you unwrap a Watt asset back into its original token, giving you flexibility in determining when the taxable event occurs\*

can be used in other DeFi protocols just like the original token

* 

Would you like to know more about how the yield is accrued to liquid-staked Watt tokens? Head over to the [Token ratio](https://docs.watt.si/protocol-overview/watt-assets/token-ratio) section.

*\*It does not constitute a tax advice. We do not know the tax implications in your specific jurisdiction. Always consult a qualified tax advisor.*

# **Token ratio**

Understanding the Token ratio is straightforward yet crucial. Watt Protocol employs the **Token ratio to determine how many liquid-staked Watt tokens you receive when wrapping, and how many original tokens you reclaim upon unwrapping.**

The Token ratio is calculated by dividing the amount of original tokens stored securely in the vault (tokens are deposited into the vault upon wrapping) by the total supply of minted Watt tokens.

With each protocol transaction, a portion of the collected fees is dedicated to burning Watt tokens. Burning reduces the total token supply, which in turn increases the Token ratio. Consequently, unwrapping tokens at a higher Token ratio yields a greater amount of original tokens, effectively distributing accrued yield to liquid-staked Watt token holders. Thus, each protocol transaction contributes positively to the yield of liquid-staked Watt tokens.

The exact APR is always displayed within the application interface.

The [Burn rate](https://docs.watt.si/protocol-overview/fee-structure/burn-rate) parameter controls the proportion of fees specifically allocated for burning liquid-staked Watt tokens.

# **Watt token specification**

What are Watt assets from technical perspective?

* Watt assets are SPL tokens utilizing the **Token-2022** transfer fee extension.  
* Each token includes a built-in fee structure (see the [Fee structure](https://docs.watt.si/protocol-overview/fee-structure) section for more information).  
* Only traditional SPL tokens without extensions can be wrapped.  
* Wrapping **mints** new Watt tokens.  
* Unwrapping **burns** existing Watt tokens.  
* Yield accrues via the **burning** of Watt assets. This mechanism increases the ratio of original tokens to Watt tokens during wrap and unwrap actions (see [Token ratio](https://docs.watt.si/protocol-overview/watt-assets/token-ratio) section).

# **Liquidity pools**

To ensure smooth functioning of the protocol, each Watt asset has a **dedicated liquidity pool on Raydium**. The simultaneous existence of both an original token liquidity pool and a Watt asset liquidity pool creates opportunities for arbitraging price differences between them. This arbitrage activity serves as one of the primary yield drivers for Watt asset holders and liquidity providers.

The protocol enables users to create Raydium CPMM pools using liquid-staked Watt tokens, allowing them to **earn both Raydium APR and Watt APR**.

Watt liquidity pools:

* are deployed on Raydium CPMM.  
* require a minimum level of liquidity to be visible and selectable within the app's user interface.  
* earn a share of the protocol's fees, which must be actively claimed by the liquidity providers.  
* can help offset impermanent loss by providing yield from both Raydium and Watt sources.

# **User actions**

Below is a simplified overview of all fundamental user actions and their consequences in the Watt Protocol.  
![][image7]

# **Fee structure**

Although often perceived as unnecessary or redundant, fee distribution in Watt protocol plays a pivotal role by unlocking arbitrage opportunities otherwise inaccessible to most of Solana users.  
Each Watt liquid-staked token carries a **specific fee configuration** at the token level. This fee structure maintains the volatility farming flywheel. Initial token wrappers and liquidity providers determine the optimal fee structure. The table below outlines the fees associated with each applicable action.  
Fee  
Allowed range  
Note  
Wrap fee  
0 \- 10%  
The sum of wrap and unwrap fee must be greater than 0.8%  
Unwrap fee  
0.4 \- 10%  
The sum of wrap and unwrap fee must be greater than 0.8%  
Burn rate  
10 \- 50%  
See explanation in [Burn rate](https://docs.watt.si/protocol-overview/fee-structure/burn-rate)  
Buy or sell fee  
0.55 \- 4%  
Recognized as a transfer fee, applies on any swap or transfer between wallets

It is generally advisable to set higher fees for more volatile assets, such as meme or AI tokens, while adopting a more conservative approach for less volatile assets like utility or governance tokens.

A small protocol fee is collected following each fee deduction to support the sustainable growth and expansion of the protocol.

Once established, the fee structure cannot be altered from the app interface.

# **Burn rate**

Make sure you understand how the [Token ratio](https://docs.watt.si/protocol-overview/watt-assets/token-ratio) works before exploring the Burn rate.

**Burn rate indicates how incurred fees are split between burning liquid-staked Watt tokens and rewarding liquidity providers in the Watt token pool.** For example, if the Burn rate is set at 40% for a certain token, this means 40% of eligible fees are dedicated to burning Watt tokens, while the remaining 60% of eligible fees are distributed among liquidity providers in a Raydium pool.

Increasing the Burn rate favours Watt token holders, whereas decreasing the Burn rate favours liquidity providers.

# **Amplifiers**

An amplifier is a unique designation for a user who decides to **provide initial liquidity** into a liquidity pool with Watt token. Amplifiers receive 100% of the *amplifier fee* as long as their liquidity position remains active.

Currently, the amplifier status is invite-only. If you want to become one of honourable amplifiers, reach us on Discord or at wattsup@watt.si.


# ** Contact**

Watt protocol Discord: https://discord.gg/cChe5CwQrh
Watt protocol Twitter/X: @watt_protocol
Watt protocol Website: watt.si
Watt protocol Email: wattsup@watt.si