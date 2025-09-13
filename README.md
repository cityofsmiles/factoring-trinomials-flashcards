# Factoring Trinomials Flashcards

An interactive web app for practicing factoring trinomials through flashcards.  
Hosted at: [https://cityofsmiles.github.io/factoring-trinomials-flashcards](https://cityofsmiles.github.io/factoring-trinomials-flashcards)

## Features

- Randomized flashcards for each session (10 per set)
- Type your answers in factored form (e.g., `(2x + 1)(x - 9)`)
- Instant feedback for each response
- Review all answers with a detailed answer key and score
- Option to retry with a new shuffled set

## How It Works

1. A set of 10 trinomials is loaded from `flashcards.json`.
2. The app presents each trinomial one at a time.
3. You type your answer in factored form.
4. After completing all flashcards, submit to see your score and the answer key.

## Development

This project is built with React and uses **Framer Motion** for animations.

### Run Locally

```bash
# Clone the repository
git clone https://github.com/cityofsmiles/factoring-trinomials-flashcards.git

# Navigate to the project folder
cd factoring-trinomials-flashcards

# Install dependencies
npm install

# Start development server
npm run dev
```

### Build for Production

```bash
npm run build
```

The production-ready files will be output to the `dist/` folder.

## File Structure

- `App.jsx` â€” main React component handling flashcards, answers, and results
- `flashcards.json` â€” question and answer data (loaded dynamically)
- `flashcards.css` â€” styling for flashcards and UI elements

## Data Format

`flashcards.json` is an array of objects:

```json
[
  {
    "question": "x^2 + 5x + 6",
    "answer": "(x + 2)(x + 3)"
  },
  {
    "question": "2x^2 - 8x - 24",
    "answer": "2(x - 6)(x + 2)"
  }
]
```

## Credits

Developed by **Jonathan R. Bacolod, LPT**.
