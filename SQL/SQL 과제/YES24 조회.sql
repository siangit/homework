-- SELECT title, author from Books
-- SELECT * from Books
-- SELECT title from Books where rating >= 8.0
-- SELECT title, review from Books where review >= 100
-- SELECT title, price from Books where price < 20000
-- SELECT title from Books where ranking_weeks >4
-- SELECT title from Books where author = "최경희 저"
-- SELECT title from Books where publisher ="난다"

-- SELECT * from Books
-- SELECT author, COUNT(*) FROM Books GROUP BY author
-- SELECT publisher, COUNT(*) AS sales FROM Books GROUP BY publisher ORDER BY sales DESC LIMIT 1;
-- SELECT author, AVG(rating) AS avg_rating FROM Books GROUP BY author ORDER BY avg_rating DESC LIMIT 1;
-- SELECT title, author FROM Books WHERE ranking = 1;
-- SELECT title, sales, review FROM Books ORDER BY sales DESC, review DESC LIMIT 10;
-- SELECT title, publishing FROM Books ORDER BY publishing DESC LIMIT 5; 

-- SELECT author, AVG(rating) FROM Books GROUP BY author;
-- SELECT publishing, COUNT(*) FROM Books GROUP BY publishing;
-- SELECT title, AVG(price) FROM Books GROUP BY title;
-- SELECT title, AVG(price) FROM Books GROUP BY title;
-- SELECT title, review FROM Books ORDER BY review DESC LIMIT 5;
SELECT ranking, AVG(review) FROM Books GROUP BY ranking;