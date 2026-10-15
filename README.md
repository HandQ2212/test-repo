# ⚡ Pulse & Vitality — Health & Human Performance Knowledge Hub

Evidence-based scientific knowledge hub for Sleep, Recovery, Activity, and Longevity, mapped directly to real-time wearable biometrics.

Curated from clinical standards and physiological methodologies developed by **Flo Health, Clue, Natural Cycles, Fitbit Blog, WHOOP The Locker, Maven Clinic**, and peer-reviewed clinical trials from **PubMed / BJU International**.

---

## 🌟 Key Features

1. **28 Full-Length Evidence-Based Blog Articles**:
   - **Sleep** (4 articles): Sleep Score algorithms, Deep Sleep vs REM, Slow Wave Sleep protocol, Sleep Debt accumulation.
   - **Recovery** (4 articles): Heart Rate Variability (HRV), Overnight Resting Heart Rate, 5.5s Coherence Breathing, Active vs Passive Recovery.
   - **Activity** (4 articles): Active Zone Minutes (AZM), Day Strain (0–21), Zone 2 Cardio Blueprint, Overtraining Syndrome.
   - **Health & Wellness** (4 articles): Wearable Stress Score, Cardio Fitness / VO2 Max, Vagus Nerve Activation, Thermal Contrast Therapy.
   - **Women's Health** (6 articles): 4 Menstrual Phases, Cervical Fluid Types, BBT Thermal Shift, Cycle-Synced Fitness, 6-Day Fertile Window, PMS Nutrition.
   - **Men's Health** (6 articles): Pelvic Floor Anatomy (PC & BC muscles), Kegel Contraction Protocols, Clinical Trials on ED/PE, Stamina Conditioning, Groin Stretching, Mind Cleaner.

2. **Dual-Format Delivery**:
   - **Full Blog Page View (`Discover more`)**: Full-screen editorial magazine format with reading progress bar, hero headlines, author cards, key takeaway banners, and canonical study citations.
   - **In-App Mobile Simulator (`Learn more`)**: Bottom-sheet modal mockup simulating wearable mobile app icon `(i)` clicks.

3. **Standalone Static HTML Pages**:
   - 28 pre-rendered standalone `.html` files in `posts/` for independent sharing, linking, or offline reading without any dependencies.

4. **Master Research Documentation**:
   - Located in `docs/Master_Health_Articles_MVP.xlsx` with complete 3-sheet schema (`Master_Content_MVP`, `Mapping_Matrix`, `HDSD_Data_Schema`).

---

## 🚀 How to Deploy on Render

### Option 1: Static Site (Fastest & Free)
1. In your [Render Dashboard](https://dashboard.render.com/), click **New +** → **Static Site**.
2. Connect your GitHub repository: `HandQ2212/test-repo`.
3. Configure settings:
   - **Name**: `pulse-vitality-hub` (or any name)
   - **Branch**: `main`
   - **Build Command**: *(leave empty)*
   - **Publish Directory**: `.`
4. Click **Create Static Site**. Your site will be live in seconds!

### Option 2: Web Service (Node.js)
1. Click **New +** → **Web Service**.
2. Connect `HandQ2212/test-repo`.
3. Configure settings:
   - **Runtime**: `Node`
   - **Build Command**: *(leave empty or `npm install`)*
   - **Start Command**: `node server.js`
4. Click **Create Web Service**.

---

## 💻 Local Development

Run with Node.js:
```bash
node server.js
# Opens on http://localhost:3000
```

Or run directly with Python:
```bash
python3 -m http.server 3000
```

Or simply open `index.html` directly in any web browser!

