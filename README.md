# 🖼️ PicHide – Image in Image Steganography (Streamlit)

**PicHide** is a Python mini-project that demonstrates **Image Steganography** — hiding one image inside another without visibly altering the cover image.  
This app uses **Streamlit** for the UI and the **Least Significant Bit (LSB)** technique to embed and extract images.

---

## 🚀 Features

- 🔒 Hide one image inside another using LSB technique  
- 🕵️ Reveal the hidden image from the encoded image  
- 🖥️ Clean, interactive UI with Streamlit  
- 💾 Download encoded and decoded images  
- ⚡ Lightweight and runs offline

---

## 🧠 How It Works

Each pixel has three color channels (R, G, B), each stored as 8 bits. PicHide replaces the lower bits of the cover image with the higher bits of the secret image so the cover visually stays the same while carrying hidden data.

---

## 🧩 Process Overview

| Step | Input | Output |
|------|--------|--------|
| **Hide Mode**   | Cover image + Secret image | Encoded image (looks like cover) |
| **Reveal Mode** | Encoded image               | Extracted hidden image          |

Workflow:  
```
Cover Image + Secret Image → Encoded Image → Revealed Hidden Image
```

---

## ⚙️ Installation

1. Clone the repo:
```bash
git clone https://github.com/YOUR-USERNAME/PicHide.git
cd PicHide
```

2. Install dependencies:
```bash
pip install streamlit pillow numpy
```
or
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

Run:
```bash
python -m streamlit run gui_streamlit.py
```

Open your browser at: `http://localhost:8501`

---

## 🧰 Project Structure

```
PicHide/
├── gui_streamlit.py       # Main Streamlit app
├── main.py                # Core encode/decode logic (optional)
├── requirements.txt
├── README.md
└── samples/               # Example images (cover.png, secret.png)
```

---

## 💡 Future Enhancements

- Password-protected decoding  
- Encrypt secret before embedding  
- Support multiple hidden images  
- Image quality comparisons (PSNR/SSIM)

---

## 🧑‍💻 Author

**Yashasvi Velagapudi** — Developed as a mini-project on Image Steganography.

---

## 🪪 License

Open-source — free for educational and personal use.

⭐ If you find this project useful, please give it a star!
