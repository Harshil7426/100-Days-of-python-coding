## 👉 Day 95 Challenge
Today's challenge is to create a daily track generator.

Your program should:

- Pull in 5 of the most recent news stories in your area. (You could also specify a category here to avoid all the depressing stuff out there.)
- Ask openai to summarise each story in two to three words.
- Pass those words to Spotify in a search. Show and give a sample of each song.
- No need to build this in Flask today. A command line program is just fine. The console should display:
    - The name of each track (five tracks)
    - The prompt words used for the search
    - The URL to get the sample
