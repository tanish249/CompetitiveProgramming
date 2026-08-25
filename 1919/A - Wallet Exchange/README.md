<h2><a href="https://codeforces.com/contest/1919/problem/A" target="_blank" rel="noopener noreferrer">1919A — Wallet Exchange</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1919A](https://codeforces.com/contest/1919/problem/A) |

## Topics
`games` `math`

---

## Problem Statement

<div class="header"><div class="title">A. Wallet Exchange</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Alice and Bob are bored, so they decide to play a game with their wallets. Alice has $$$a$$$ coins in her wallet, while Bob has $$$b$$$ coins in his wallet.</p><p>Both players take turns playing, with Alice making the first move. In each turn, the player will perform the following steps <span class="tex-font-style-bf">in order</span>:</p><ol> <li> Choose to exchange wallets with their opponent, or to keep their current wallets. </li><li> Remove $$$1$$$ coin from the player's current wallet. The current wallet cannot have $$$0$$$ coins before performing this step. </li></ol><p>The player who cannot make a valid move on their turn loses. If both Alice and Bob play optimally, determine who will win the game.</p></div><div class="input-specification"><div class="section-title">Input</div><p>Each test contains multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 1000$$$) — the number of test cases. The description of the test cases follows.</p><p>The first and only line of each test case contains two integers $$$a$$$ and $$$b$$$ ($$$1 \le a, b \le 10^9$$$) — the number of coins in Alice's and Bob's wallets, respectively.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output "<span class="tex-font-style-tt">Alice</span>" if Alice will win the game, and "<span class="tex-font-style-tt">Bob</span>" if Bob will win the game.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id003986968908660474" id="id009086962863979616" class="input-output-copier">Copy</div></div><pre id="id003986968908660474"><div class="test-example-line test-example-line-even test-example-line-0">10</div><div class="test-example-line test-example-line-odd test-example-line-1">1 1</div><div class="test-example-line test-example-line-even test-example-line-2">1 4</div><div class="test-example-line test-example-line-odd test-example-line-3">5 3</div><div class="test-example-line test-example-line-even test-example-line-4">4 5</div><div class="test-example-line test-example-line-odd test-example-line-5">11 9</div><div class="test-example-line test-example-line-even test-example-line-6">83 91</div><div class="test-example-line test-example-line-odd test-example-line-7">1032 9307</div><div class="test-example-line test-example-line-even test-example-line-8">839204 7281</div><div class="test-example-line test-example-line-odd test-example-line-9">1000000000 1000000000</div><div class="test-example-line test-example-line-even test-example-line-10">53110 2024</div></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007037972099075589" id="id003572124736452762" class="input-output-copier">Copy</div></div><pre id="id007037972099075589">Bob
Alice
Bob
Alice
Bob
Bob
Alice
Alice
Bob
Bob
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, an example of the game is shown below:</p><ul> <li> Alice chooses to not swap wallets with Bob in step 1 of her move. Now, $$$a=0$$$ and $$$b=1$$$. </li><li> Since Alice's wallet is empty, Bob must choose to not swap their wallets in step 1 of his move. Now, $$$a=0$$$ and $$$b=0$$$. </li><li> Since both Alice's and Bob's wallets are empty, Alice is unable to make a move. Hence, Bob wins. </li></ul><p>In the second test case, an example of the game is shown below:</p><ul> <li> Alice chooses to swap wallets with Bob in step 1 of her move. Now, $$$a=3$$$ and $$$b=1$$$. </li><li> Bob chooses to swap wallets with Alice in step 1 of his move. Now, $$$a=1$$$ and $$$b=2$$$. </li><li> Alice chooses to not swap wallets with Bob in step 1 of her move. Now, $$$a=0$$$ and $$$b=2$$$. </li><li> Since Alice's wallet is empty, Bob can only choose to not swap wallets with Alice in step 1 of his move. Now, $$$a=0$$$ and $$$b=1$$$. </li><li> Since Alice's wallet is empty, Alice can only choose to swap wallets with Bob in step 1 of her move. Now, $$$a=0$$$ and $$$b=0$$$. </li><li> Since both Alice's wallet and Bob's wallet are empty, Bob is unable to make a move. Hence, Alice wins. </li></ul></div>