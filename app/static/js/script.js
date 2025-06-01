document.addEventListener('DOMContentLoaded', function() {
    const quotes = [
        "Love is composed of a single soul inhabiting two bodies. - Aristotle",
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "You know you're in love when you can't fall asleep because reality is finally better than your dreams. - Dr. Seuss",
        "Love all, trust a few, do wrong to none. - William Shakespeare",
        "In the end, the love you take is equal to the love you make. - Paul McCartney"
    ];

    const quoteElement = document.getElementById('quote');
    const randomQuoteButton = document.getElementById('random-quote-button');

    function displayRandomQuote() {
        const randomIndex = Math.floor(Math.random() * quotes.length);
        quoteElement.textContent = quotes[randomIndex];
    }

    randomQuoteButton.addEventListener('click', displayRandomQuote);

    // Display a random quote on page load
    displayRandomQuote();
});