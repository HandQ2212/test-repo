# Understanding Your Sleep Score: How Wearables Measure Overnight Recovery

- **Article ID:** `LM_SL_01`
- **Category:** Sleep — Sleep Score Algorithm
- **Content Type:** Learn more
- **Mapped App Screen & Metric:** `Sleep Screen` (`Sleep Score (0–100)`)
- **Reading Time:** 8 min
- **Hero Cover Image:** `images/LM_SL_01_hero.jpg`
- **Inline Infographic:** `images/LM_SL_01_diagram.svg`
- **Primary Reference:** [Oura Ring & Garmin Health Science / Sleep Journal (Beattie et al., 2017)](https://ouraring.com/blog/sleep-score/)

> **Executive Summary:** Every morning, your smartwatch distills hours of heart rate, HRV, movement, and breathing data into a single number from 0 to 100. Here is how leading wearables like Oura, Garmin, and WHOOP calculate your Sleep Score—and how to read your overnight graphs like a sleep scientist.

> 💡 **Key Actionable Takeaway:** Stop fixating on total hours in bed alone. A high-recovery Sleep Score (85+) depends just as much on Sleep Efficiency (≥ 85%), how early your Overnight Resting Heart Rate reaches its lowest point (Nadir), and keeping your wake time within a consistent ±30-minute daily window.

---

## Why Eight Hours in Bed Doesn't Always Equal Eight Hours of Sleep

If you have ever stayed in bed for eight full hours only to wake up feeling groggy—and opened your companion app to find a **Sleep Score of 68**—you have experienced the critical difference between *Time in Bed* and *Restorative Sleep Quality*.

Modern smartwatches and smart rings (including **Oura Ring**, **Garmin Firstbeat Analytics**, **WHOOP**, and **Fitbit**) no longer act as simple timers. While you sleep, your wearable continuously samples your pulse wave, beat-to-beat Heart Rate Variability (HRV), respiratory rate, wrist movement, and peripheral skin temperature. By morning, an algorithm synthesizes these signals into a single **0 to 100 Sleep Score** designed to answer one practical question: *How well did your body and brain actually recover last night?*

<figure class="article-inline-diagram">
  <img src="images/LM_SL_01_diagram.svg" alt="Sleep Score Architecture & Multi-Sensor Contributors" loading="lazy">
  <figcaption>📊 <strong>Wearable Biometric Architecture:</strong> How optical PPG heart rate, HRV, movement (actigraphy), and sleep stage balance combine to build your daily 0–100 Sleep Score.</figcaption>
</figure>

---

## The 6 Core Contributors Behind Your Sleep Score

Leading wearable platforms evaluate sleep as a multi-dimensional system rather than a single stopwatch. On platforms like **Oura** and **Garmin**, your daily Sleep Score is weighted across six physiological pillars:

| Sleep Score Contributor | Ideal Target Range | Weight | What Your Watch Is Actually Measuring |
| :--- | :--- | :--- | :--- |
| **1. Total Sleep Time (TST)** | **7h 30m – 8h 30m** | ~25% | Actual time spent in Light, Deep, and REM sleep—explicitly subtracting brief awake micro-arousals during the night. |
| **2. Sleep Efficiency** | **≥ 85% (Optimal ≥ 90%)** | ~20% | The percentage of your total time in bed actually spent asleep: `Sleep Efficiency = (Total Sleep Time ÷ Time in Bed) × 100`. |
| **3. Restfulness & Disturbances** | **Minimal Wakeups & Tosses** | ~15% | Frequency of movement spikes detected by the 3-axis accelerometer and brief heart-rate surges caused by fragmented sleep. |
| **4. Deep Sleep (Slow-Wave)** | **15% – 25% of TST (~60–110 min)** | ~15% | Physical tissue repair, human growth hormone (HGH) release, and immune restoration occurring mainly in the first half of the night. |
| **5. REM Sleep** | **20% – 25% of TST (~90–120 min)** | ~15% | Cognitive restoration, memory consolidation, and emotional processing concentrated in the final third of the night. |
| **6. Timing & Sleep Latency** | **10 – 20 mins to fall asleep** | ~10% | How closely your sleep midpoint aligns with your natural circadian night, plus how quickly you transition from lying down to asleep. |

> **Wearable Pro Tip — Watch Your Sleep Latency:** Taking **10 to 20 minutes** to fall asleep is the clinical sweet spot. If your app shows you fall asleep in **under 5 minutes** every night, it is rarely a sign of "great sleep skill"—clinical sleep medicine (and WHOOP/Oura data) recognizes ultra-short latency as a primary indicator of accumulated **Sleep Debt**.

---

## How Your Watch Knows You're Asleep: Inside the Sensors

Historically, measuring sleep required an overnight hospital **Polysomnography (PSG)** test using scalp EEG electrodes, eye-movement sensors, and muscle leads. Today's wearables bridge the gap between lab-grade sleep medicine and everyday life using **Multi-Sensor Data Fusion**:

1. **Optical Heart Rate (PPG) & Autonomic Shifting:** Green and infrared LEDs on the back of your device measure microscopic changes in blood volume with every heartbeat. As you transition from wakefulness into Light and Deep sleep, your parasympathetic ("rest-and-digest") nervous system takes over—slowing your heart rate and increasing beat-to-beat **Heart Rate Variability (HRV)**.
2. **3-Axis Accelerometry (Micro-Actigraphy):** High-frequency motion sensors track wrist or finger stillness down to fractions of a gravity unit (`g`), separating quiet screen-reading in bed from true physiological sleep onset.
3. **Respiratory Rate Stability:** Using variations in your pulse wave (Respiratory Sinus Arrhythmia), your watch tracks breaths per minute. Breathing becomes remarkably slow and rhythmic during Deep sleep, then turns faster and more irregular during vivid REM dreaming.

In a landmark validation study published in the journal *Sleep* (**Beattie et al., 2017**), researchers compared multi-sensor consumer wearables combining optical PPG and accelerometry against gold-standard hospital Polysomnography. They demonstrated that multi-sensor wearables achieve **>90% sensitivity in detecting true sleep vs. wakefulness** and reliable 4-stage sleep tracking—a massive leap beyond older motion-only fitness bands.

<figure class="article-inline-photo">
  <img src="images/LM_SL_01_photo.jpg" alt="Reviewing overnight sleep score and heart rate curve on a smartwatch" loading="lazy">
  <figcaption>📷 <strong>Morning Biometric Check-In:</strong> Reviewing your overnight heart rate curve (the "Hammock Curve") reveals far more about recovery quality than total hours alone.</figcaption>
</figure>

---

## Reading Your Overnight Heart Rate Graph: The "Hammock Curve" vs. The "Downward Slope"

One of the highest-value insights popularized by **Oura Ring** and **WHOOP** is examining the **shape** of your overnight resting heart rate curve— specifically when your heart rate reaches its lowest overnight point (**RHR Nadir**):

### 1. The Restorative "Hammock" Curve (Score 85–100)
When you finish eating early, wind down in dim light, and go to bed well-hydrated, your heart rate drops rapidly shortly after sleep onset. It reaches its **lowest point (Nadir) near the middle of the night**, then gently rises just before you wake up to prepare your body for the day. Visually, the graph looks like a smooth **U-shape or hammock**.

### 2. The Exhaustion "Downward Slope" (Score 60–74)
Have you ever slept 8 hours after a heavy late dinner, evening drinks, or a 9:00 PM workout, only to see a mediocre Sleep Score? Look at your overnight heart rate line:
- Instead of dropping right away, your heart rate remains elevated (`65–75+ bpm`) for the first 3 to 4 hours of the night while your body works overtime to digest food, metabolize alcohol, or clear stress hormones.
- Your heart rate only reaches its lowest point **right before your alarm goes off**—forming a downward slope instead of a hammock. Because your body spent the first half of the night in a high-metabolic state, your early-night **Deep Sleep** is significantly compressed.

---

## How to Interpret Your Score Tiers

| Score Tier | Rating | How Your Body Feels & How to Train Today |
| :--- | :--- | :--- |
| **85 – 100** | **Optimal Readiness** | Autonomic nervous system is fully recharged. Sleep efficiency is high, RHR reached its lowest point early, and Deep/REM cycles completed. **Green light for high-intensity training or demanding cognitive work.** |
| **70 – 84** | **Good / Baseline** | Solid maintenance sleep. One contributor—often slightly short duration, mild restlessness, or a late bedtime—held the score back. **Maintain normal daily activity and moderate training.** |
| **Below 70** | **Pay Attention / Recovery Needed** | Significant sleep fragmentation, elevated overnight heart rate, or acute sleep debt. **Prioritize Zone 1–2 active recovery, hydration, early sunlight, and an earlier wind-down tonight.** |

---

## 4 Proven Habits to Raise Your Sleep Score Tonight

1. **Follow the 3-2-1 Evening Wind-Down Rule:**
   - **3 Hours Before Bed:** Finish your last large meal and avoid alcohol so digestion and liver metabolism don't elevate your early-night heart rate.
   - **2 Hours Before Bed:** Wrap up stressful work emails and intense cardio so cortisol and core temperature can drop naturally.
   - **1 Hour Before Bed:** Dim overhead LED lights and put away bright screens to allow natural melatonin release.
2. **Anchor Your Wake Time Within ±30 Minutes:** Your circadian rhythm is anchored primarily by when you wake up and view morning light—not just when you go to bed. Keeping your wake time consistent (even on weekends) stabilizes Sleep Efficiency and REM timing.
3. **Cool Your Bedroom to 18.3°C (65°F):** Your core body temperature must drop by roughly **1.0°C (1.8°F)** to initiate and sustain Deep Slow-Wave Sleep. A cool room prevents mid-night thermal micro-arousals.
4. **Track Your 7-Day Rolling Trend, Not Just One Bad Night:** As Garmin and WHOOP sports scientists emphasize, a single score of 65 before a big race or presentation won't ruin your performance if your 7-day rolling average is above 80. Use low scores as helpful feedback, never as a source of sleep anxiety.

---

## References & Clinical Sources

1. **Beattie, Z., Oyang, Y., Statan, A., Ghoreyshi, A., Pantelopoulos, A., Russell, A., & Heneghan, C. (2017).** *Estimation of sleep stages in a healthy adult population from optical plethysmography and accelerometer signals.* Physiological Measurement / Sleep, 38(11), 1968–1979. [Read on PubMed / NIH ↗](https://pubmed.ncbi.nlm.nih.gov/28960186/)
2. **de Zambotti, M., Cellini, N., Goldstone, A., Colrain, I. M., & Baker, F. C. (2019).** *Wearable Sleep Technology in Clinical and Research Settings.* Medicine & Science in Sports & Exercise, 51(7), 1538–1557. [Read on PubMed / NIH ↗](https://pubmed.ncbi.nlm.nih.gov/30789439/)
3. **Oura Ring Pulse Blog.** *How Oura Measures Sleep & Calculates Your Sleep Score.* [Read on Oura Ring ↗](https://ouraring.com/blog/sleep-score/)
4. **Garmin Health Science & Firstbeat Analytics.** *Sleep Tracking & Sleep Score Technology.* [Read on Garmin Health Science ↗](https://www.garmin.com/en-US/garmin-technology/health-science/sleep-tracking/)
