from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)
def load_data():
    udemy1_df = pd.read_excel("Udemy1.xlsx")
    udemy2_df = pd.read_excel("Udemy2.xlsx")  
    edx_df = pd.read_excel("Edx.xlsx")
    coursera_df = pd.read_excel("Coursera.xlsx")
    udemy1_df["Site"] = "Udemy"
    udemy2_df["Site"] = "Udemy"  
    edx_df["Site"] = "EdX"
    coursera_df["Site"] = "Coursera"
    all_data = pd.concat([udemy1_df, udemy2_df, edx_df, coursera_df], ignore_index=True)
    all_data["Course_Price"] = "Paid"  
    return all_data
df = load_data()
@app.route('/')
def about():
    return render_template('about.html')
@app.route('/courses')
def index():
    category = request.args.get('category', '')
    level = request.args.get('level', '')
    rating = request.args.get('rating', '')
    filtered_df = df.copy()
    if category:
        filtered_df = filtered_df[filtered_df['Course_Category'] == category]
    if level:
        filtered_df = filtered_df[filtered_df['Course_Level'] == level]
    if rating:
        filtered_df = filtered_df[filtered_df['Course_Rating'] >= float(rating)]
    categories = sorted(df['Course_Category'].dropna().unique())
    levels = sorted(df['Course_Level'].dropna().unique())
    return render_template('index.html',
                           courses=filtered_df.to_dict(orient='records'),
                           categories=categories,
                           levels=levels,
                           selected_category=category,
                           selected_level=level,
                           selected_rating=rating)
if __name__ == '__main__':
    app.run(debug=True)