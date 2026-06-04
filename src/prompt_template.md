Go to heb.com and add ingredients to my cart for a 2-week 
dinner+snack+dessert plan. Do NOT checkout — I'll review 
and handle substitutions live as you shop.

ABOUT ME: 40yo male, eating solo. Active — lifting weights 
and indoor climbing 3x/week. I handle breakfast myself; 
lunch = leftovers from the previous night's dinner.

THEMES: Week 1 = {{WEEK1_THEME}}, Week 2 = {{WEEK2_THEME}}.
Each recipe should clearly fit its theme.

DINNERS (14 nights total, 7 per theme):
- Every recipe scaled to 2 servings: 1 eaten that night 
  for dinner, 1 packed as next-day lunch.
- Vary proteins across fish (frozen is fine), pork, 
  chicken, beef. NO shrimp, lobster, crab, crayfish, or 
  any crustacean.
- Per serving target: ~600-800 kcal, 35-45g protein. 
  Complex carbs, healthy fats, minimize ultra-processed.

SNACKS: ~3 per day, varied across the 2 weeks. Mix 
whole-food (Greek yogurt, cottage cheese, fruit, nuts, 
jerky, hummus + veg, edamame, string cheese, olives) 
with a few packaged options (protein bars, dark 
chocolate). Lean protein-forward.

DESSERT: 3-4x per week, lighter side — fruit-based, 
dark chocolate, yogurt parfaits, or modest themed treats.

PANTRY ALREADY ON HAND (do not re-buy): olive oil, salt, 
black pepper, garlic, common dried herbs (oregano, thyme, 
basil, rosemary, paprika), soy sauce, vinegar, flour, 
sugar. Buy theme-specific items as needed (miso, tahini, 
gochujang, fish sauce, harissa, etc.).

BUDGET: $260 hard cap on the cart total. Keep a running 
total visible as you add items. If you're heading over, 
pause before the last few items so I can choose what to 
cut.

BEFORE ADDING ANYTHING TO THE CART, create and save a 
local HTML file named "meal-plan-{{WEEK1_THEME}}-{{WEEK2_THEME}}.html" 
using the structure below, then share the file with me 
in chat. Only start adding items to the HEB cart after 
I have the HTML file.

HTML FILE REQUIREMENTS:
The file must use this exact structure and CSS styling:

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2-Week {{WEEK1_THEME}} / {{WEEK2_THEME}} Meal Plan</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #333; line-height: 1.6; padding: 20px; }
    .container { max-width: 1000px; margin: 0 auto; background: white; border-radius: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.3); overflow: hidden; }
    header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 40px 30px; text-align: center; }
    header h1 { font-size: 2.5em; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
    header p { font-size: 1.1em; opacity: 0.95; }
    .content { padding: 40px 30px; }
    .section-title { background: #f8f9fa; padding: 20px; margin: 30px 0 20px 0; border-left: 5px solid #667eea; font-size: 1.8em; color: #333; }
    .recipe { background: #f8f9fa; border: 2px solid #e9ecef; border-radius: 8px; padding: 25px; margin-bottom: 25px; transition: all 0.3s ease; }
    .recipe:hover { border-color: #667eea; box-shadow: 0 5px 20px rgba(102,126,234,0.2); }
    .recipe h2 { color: #667eea; font-size: 1.6em; margin-bottom: 10px; }
    .recipe-meta { display: flex; gap: 20px; flex-wrap: wrap; font-size: 0.95em; color: #666; margin-bottom: 15px; }
    .ingredients { background: white; padding: 15px; border-radius: 6px; margin: 15px 0; }
    .ingredients h3, .instructions h3 { color: #764ba2; margin-bottom: 10px; font-size: 1.2em; }
    .ingredients ul { list-style: none; padding-left: 0; }
    .ingredients li { padding: 8px 0 8px 25px; position: relative; }
    .ingredients li:before { content: "✓"; position: absolute; left: 0; color: #667eea; font-weight: bold; }
    .instructions { background: white; padding: 15px; border-radius: 6px; margin: 15px 0; }
    .instructions ol { padding-left: 20px; }
    .instructions li { margin-bottom: 10px; padding-left: 8px; }
    .meal-plan { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0; }
    .meal-day { background: white; border: 2px solid #e9ecef; border-radius: 8px; padding: 15px; text-align: center; }
    .meal-day h3 { color: #667eea; margin-bottom: 10px; }
    .meal-day p { color: #666; font-size: 0.95em; }
    .equipment { background: #f0f4ff; border: 2px dashed #667eea; border-radius: 8px; padding: 20px; margin: 20px 0; }
    .equipment h3 { color: #764ba2; margin-bottom: 15px; }
    .equipment-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; }
    .equipment-item { background: white; padding: 10px; border-radius: 6px; text-align: center; border-left: 4px solid #667eea; }
    .shopping-summary { background: #fff3cd; border: 2px solid #ffc107; border-radius: 8px; padding: 20px; margin: 20px 0; }
    .shopping-summary h3 { color: #856404; margin-bottom: 10px; }
    .shopping-categories { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; }
    .shopping-cat { background: white; padding: 10px; border-radius: 6px; text-align: center; }
    footer { background: #f8f9fa; padding: 20px 30px; text-align: center; border-top: 1px solid #e9ecef; color: #666; }
    @media print { body { background: white; } .recipe { page-break-inside: avoid; } }
    @media (max-width: 768px) { header h1 { font-size: 1.8em; } .content { padding: 20px; } .recipe { padding: 15px; } }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🍽️ {{WEEK1_THEME}} / {{WEEK2_THEME}} Meal Plan</h1>
      <p>2 Weeks of Healthy Dinners</p>
      <p style="font-size:0.9em;margin-top:10px;">14 Complete Recipes • Budget-Friendly • Prep Times Included</p>
    </header>
    <div class="content">

      <!-- EQUIPMENT SECTION -->
      <div class="section-title">🛠️ Kitchen Equipment Needed</div>
      <div class="equipment">
        <h3>Essential Equipment & Tools</h3>
        <div class="equipment-list">
          [one .equipment-item div per tool needed across all 14 recipes]
        </div>
      </div>

      <!-- 2-WEEK MEAL PLAN OVERVIEW -->
      <div class="section-title">📅 2-Week Meal Plan Overview</div>
      <div class="meal-plan">
        [one .meal-day div per day, Days 1–14]
      </div>

      <!-- SHOPPING SUMMARY -->
      <div class="section-title">🛒 Shopping Summary</div>
      <div class="shopping-summary">
        <h3>What's in Your Cart (N Items)</h3>
        <div class="shopping-categories">
          [category counts: Proteins, Vegetables, Spices, Pantry, Snacks, Desserts, Dairy]
        </div>
        <p style="margin-top:15px;text-align:center;"><strong>Total Budget: $X.XX</strong></p>
      </div>

      <!-- WEEK 1 RECIPES -->
      <div class="section-title">🍽️ WEEK 1 — {{WEEK1_THEME}} (Days 1–7)</div>
      [7 .recipe divs, each with: h2 day+name, .recipe-meta servings/prep/cook,
       .ingredients ul, .instructions ol]

      <!-- WEEK 2 RECIPES -->
      <div class="section-title">🍽️ WEEK 2 — {{WEEK2_THEME}} (Days 8–14)</div>
      [7 .recipe divs, same structure]

    </div>
    <footer>Generated for your 2-week meal plan • {{WEEK1_THEME}} & {{WEEK2_THEME}}</footer>
  </div>
</body>
</html>

Save the file to the Desktop. Once you confirm it is saved, begin adding 
items to the HEB cart with a running total. Flag anything out of stock 
so I can substitute live.
