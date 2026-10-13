# So we have a review csv and we have generate a summary and a sentiment

from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenRouter(
    model = "nvidia/nemotron-3.5-lightning:free",
    temperature=0.7,
)

# schema
class Review(TypedDict):
    summary: str
    sentiment: str
    key_themes: Annotated[list[str], "List down some themes discussed in the review"] # We can also pass an explicit direction for the variable with Annotated
    advice: Annotated[Literal["Buy", "Don't Buy"], " Return a piece of advice for the purchase"] # Literal -> Choose only between options
    name: Annotated[Optional[str], "write the name of the reviewer"] # Optional -> any value or None
    saints: Annotated[Optional[list[str]], "Write the names of saints given in the prompt"]

structured_output = model.with_structured_output(Review)

result = structured_output.invoke("""## Pixel 9 vs iPhone 15 — Full Review

---

### Design & Build

The **Pixel 9** is a noticeable shift for Google — flat sides, a centered camera bar, and a recycled aluminium frame behind Gorilla Glass Victus 2. It's solid but chunky at **198 g** and 8.5 mm thick. The **iPhone 15** is the lighter, slimmer option at **171 g** and 7.8 mm, with its Ceramic Shield front and glass back. If you care about pocket feel, the iPhone wins by a clear margin. The Pixel's colours (Peony, Wintergreen, Porcelain, Obsidian) are more muted; the iPhone's palette is bolder.

**Winner: iPhone 15** (lighter, slimmer, more refined in hand)

---

### Display

| | Pixel 9 | iPhone 15 |
|---|---|---|
| Size | 6.3" | 6.1" |
| Resolution | 2424 × 1080 (422 ppi) | 2556 × 1179 (460 ppi) |
| Refresh Rate | **120 Hz** (LTPO) | 60 Hz |
| Peak Brightness | 2700 nits | 2000 nits |
| HDR | HDR10+ | HDR10, Dolby Vision |

This is the single biggest gap between the two phones. The Pixel 9's **120 Hz LTPO** panel is a massive upgrade over the iPhone 15's 60 Hz Super Retina XDR. Scrolling, gaming, and animation all feel noticeably smoother. The iPhone does have a slightly higher pixel density and supports Dolby Vision, but the 120 Hz vs 60 Hz difference is the kind of thing you feel immediately and can't un-see.

**Winner: Pixel 9** (120 Hz is a game-changer)

---

### Performance

| | Pixel 9 | iPhone 15 |
|---|---|---|
| Chip | Tensor G4 (4 nm) | A16 Bionic (4 nm) |
| CPU | Octa-core, up to 3.1 GHz | Hexa-core, up to 3.46 GHz |
| GPU | Mali-G715 MC7 | 5-core Apple GPU |
| RAM | **12 GB** | 6 GB |
| GeekBench 6 (Single) | ~1707 | **~2592** |
| GeekBench 6 (Multi) | ~7536 | **~11,400** |

On raw benchmarks, the **A16 Bionic** is significantly faster — roughly **52% faster in single-core** and **49% faster in multi-core**. However, in real-world daily use (social media, browsing, apps), both phones feel equally smooth. The Pixel's 12 GB of RAM gives it more headroom for heavy multitasking and future AI workloads. The Tensor G4 does tend to run warmer under sustained load, which is a known Tensor weakness.

**Winner: iPhone 15** (raw speed), but the Pixel 9 is perfectly adequate for daily use.

---

### Camera

| | Pixel 9 | iPhone 15 |
|---|---|---|
| Main | 50 MP, f/1.69 | 48 MP, f/1.6 |
| Ultra-wide | **48 MP**, f/1.7, 123° | 12 MP, f/2.4, 120° |
| Selfie | 10.5 MP | **12 MP** + TrueDepth |
| Optical Zoom | 2x | 2x |
| Super Zoom | 9x (computational) | 15x (digital) |
| Video | 4K 60fps, 10-bit HDR | 4K 60fps, Dolby Vision, Action Mode |
| DxOMark | 143 (Photo 152, Video 126) | **145** (Photo 147, Video 153) |

This is closer than you'd think. The **Pixel 9** has a much better ultrawide (48 MP vs 12 MP — a huge difference for group shots and landscapes) and leans heavily on computational photography — Magic Editor, Best Take, and AI-powered editing are genuinely useful. The **iPhone 15** edges ahead on video (Dolby Vision, Action Mode, better stabilization) and its main camera sensor is slightly larger (1/1.56" vs 1/1.31"). Selfies are better on the iPhone thanks to the 12 MP TrueDepth sensor.

If you shoot mostly **photos and use editing tools**, the Pixel 9 is more fun. If you shoot **video or care about cinematic output**, the iPhone 15 has the edge.

**Winner: Slight edge to Pixel 9** for photography, **iPhone 15** for video.

---

### Battery & Charging

| | Pixel 9 | iPhone 15 |
|---|---|---|
| Capacity | **4,700 mAh** | 3,349 mAh |
| Wired Charging | **27W** (55% in 30 min) | 20W (50% in 30 min) |
| Wireless | 15W (Pixel Stand) | 15W (MagSafe) / 7.5W (Qi) |
| Reverse Wireless | No | **Yes (4.5W)** |
| Battery Life (video) | ~24 hrs | ~20 hrs |
| Battery Life (web) | ~10 hrs | ~10.8 hrs |

The Pixel 9's **4,700 mAh** battery is 40% larger than the iPhone 15's 3,349 mAh, and it shows. In most real-world tests, the Pixel 9 lasts **14% longer** overall. The iPhone 15 does edge out slightly on web browsing and standby, but the Pixel wins on video playback and overall endurance. Charging speeds are comparable, though the Pixel is slightly faster. The iPhone has the unique advantage of **reverse wireless charging** (you can charge AirPods/Apple Watch on the back).

**Winner: Pixel 9** (bigger battery, longer life)

---

### Software & Features

| | Pixel 9 | iPhone 15 |
|---|---|---|
| OS | Android 14 | iOS 17/18 |
| AI | **Gemini AI**, Magic Editor, Call Screen | Apple Intelligence |
| Updates | **7 years** | 5 years |
| Biometrics | Fingerprint + Face | **Face ID** |
| Dynamic Island | No | **Yes** |
| Wi-Fi | **Wi-Fi 7** | Wi-Fi 6 |
| Bluetooth | 5.3 (aptX HD) | 5.3 |
| Satellite SOS | Yes | Yes |

The Pixel 9 gets **7 years of OS updates** vs the iPhone's 5 — a significant long-term advantage. Google's AI features (Magic Editor, Call Screen, Gemini) are practical and well-integrated. Apple Intelligence is a promising platform but was still rolling out at launch. The iPhone 15 has **Face ID** (more secure and hands-free than a fingerprint sensor) and the **Dynamic Island** for notifications and live activities. The Pixel supports **Wi-Fi 7**, which is future-proofing the iPhone doesn't have.

**Winner: Pixel 9** (longer updates, Wi-Fi 7, practical AI tools)

---

### Price (India)

| | Pixel 9 | iPhone 15 |
|---|---|---|
| Starting | ₹79,999 | ₹58,900 |
| Gap | **₹21,099 more** | — |

The Pixel 9 is significantly more expensive in India. For that ₹21k premium, you get 120 Hz, 12 GB RAM, a bigger battery, and 7 years of updates — but you're also paying for a phone that's slower in raw benchmarks and lacks Face ID.

---

### Final Verdict

| Choose **Pixel 9** if you want: | Choose **iPhone 15** if you want: |
|---|---|
| 120 Hz smooth display | Lighter, slimmer phone |
| Better ultrawide camera | Better video & Dolby Vision |
| Longer battery life | Face ID |
| 7 years of updates | Apple ecosystem (Mac, iPad, Watch, AirPods) |
| Wi-Fi 7, practical AI tools | Raw processing speed |
| More RAM (12 GB) | Lower price in India |

**Overall: It's a genuine split.** The **Pixel 9** is the better *phone* on paper — 120 Hz, bigger battery, more RAM, longer updates, better ultrawide. The **iPhone 15** is the better *product* for many people — lighter, faster chip, better video, Face ID, ecosystem lock-in, and ₹21k cheaper. If you're coming from Android and want the best all-rounder, the Pixel 9 is the pick. If you're in the Apple ecosystem or value video and raw speed, the iPhone 15 still holds up well.

""")

print(result)
print(f"Final Jury : {result["advice"]}")

# Though we didn't explicitly asked to mention the summary and sentiment but with that structure in input there aroused a 
# prompt like " You are an AI assistant tht awxtracts structured insights from text. Given a product review, extract: 
# -Summary: A brief overviwes of the main points. -Sentiments: Overall tone of the review(positive, neutral, negative). 
# Return the response in JSON format.