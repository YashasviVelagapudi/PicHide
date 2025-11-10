# 🖼️ PicHide – Image in Image Steganography (Streamlit)

**PicHide** is a simple yet powerful mini-project that demonstrates **Image Steganography** — the technique of hiding one image inside another so the hidden image remains invisible to the naked eye.  
Built using **Python**, **Streamlit**, **Pillow**, and **NumPy**.

---

## 🚀 Features

- 🔒 Hide one image inside another using LSB (Least Significant Bit) technique  
- 🕵️ Reveal the hidden image perfectly from the encoded one  
- 🖥️ Interactive and modern web interface (Streamlit)  
- 💾 Download both encoded and decoded images easily  
- ⚡ Lightweight, works offline  

---

## 🧠 How It Works

1. Each pixel in an image has three color channels: **Red**, **Green**, and **Blue (RGB)**.  
2. Each color channel is represented by 8 bits (0–255).  
3. The **least significant bits (LSB)** of the cover image are replaced with the **most significant bits (MSB)** of the secret image.  
4. This change is so small that it’s invisible — the cover image looks unchanged but secretly carries the hidden image inside it.

---

## 🧩 Process Overview

| Step | Input | Output |
|------|--------|--------|
| **1️⃣ Hide Mode** | Cover image + Secret image | Encoded image (looks like cover) |
| **2️⃣ Reveal Mode** | Encoded image | Extracted hidden image |

### Example Flow

