l = ["about.txt", "portfolio.txt", "news.txt", "contact.txt"]
for i in range(len(l)):
    with open(l[i]) as about:
        a = True
        for line1 in about:
            if a:
                print(f"<h1>{line1.strip()}</h1>")
                a = False
            else:
                print(f"<p>{line1.strip()}</p>")
        print("<hr/>")
        print("<ul>")
        print('    <li><a href="portfolio.html">Our Portfolio</a></li>')
        print('    <li><a href="news.html">Latest News</a></li>')
        print('    <li><a href="contact.html">Contact Us</a></li>')
        print("</ul>")
'''with open("portfolio.txt") as portfolio:
    for line2 in portfolio:
        print(f"<h1>{line2.strip()}</h1>")
with open("news.txt") as news:
    for line3 in news:
        print(f"<h1>{line3.strip()}</h1>")
with open("contact.txt") as contact:
    for line4 in contact:
        print(f"<h1>{line4.strip()}</h1>")'''
