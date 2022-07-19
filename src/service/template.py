def template(full_name,skill,level):
    """
        beginner certificate design
        :parameter:
            full_name
            skill

        :return:
            string template html
    """
    level_bg= {"beginner":"https://cdn.stocksnap.io/img-thumbs/960w/business-workplace_JXCKDAOAKG.jpg",
                "intermediate":"https://cdn.stocksnap.io/img-thumbs/960w/business-workplace_JXCKDAOAKG.jpg",
                "advanced":"https://cdn.stocksnap.io/img-thumbs/960w/business-workplace_JXCKDAOAKG.jpg"
                } 
    return f""" 
        <html>
        <head>
        <title>Certificate</title>
        </head>
        <body style="font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 14px;
        line-height: 1.42857143;
        color: #333;
        ">
        <div style="text-align: center; position:absolute; background-size:cover;overflow:hidden;">
        <img src="{level_bg[level.lower()]}" alt="bg-cert">
        </div>
        <h1>Certificate</h1>
        <p>
        <b>Name:</b> {full_name}
        </p>
        <p>
        <b>Skill:</b> {skill}
        </p>
        <p>
        <b>Skill:</b> Beginner
        </p>
        </body>
        </html>
        """

   