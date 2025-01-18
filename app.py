from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

class AstrologyCalculator:
    def __init__(self, date, time, lat=0, lon=0):
        self.datetime_str = f"{date} {time}"
        self.datetime_obj = datetime.strptime(self.datetime_str, "%Y-%m-%d %H:%M")
        self.lat = lat
        self.lon = lon
        
    def calculate_western_zodiac(self):
        """Calculate Western zodiac sign and its characteristics"""
        day = self.datetime_obj.day
        month = self.datetime_obj.month
        
        zodiac_info = {
            "Aries": {
                "element": "Fire",
                "quality": "Cardinal",
                "ruler": "Mars",
                "traits": ["Confident", "Energetic", "Leadership"],
                "favorable_times": ["Morning", "Spring"]
            },
            "Taurus": {
                "element": "Earth",
                "quality": "Fixed",
                "ruler": "Venus",
                "traits": ["Patient", "Reliable", "Determined"],
                "favorable_times": ["Evening", "Spring"]
            },
            "Gemini": {
                "element": "Air",
                "quality": "Mutable",
                "ruler": "Mercury",
                "traits": ["Adaptable", "Communicative", "Curious"],
                "favorable_times": ["Morning", "Late Spring"]
            },
            "Cancer": {
                "element": "Water",
                "quality": "Cardinal",
                "ruler": "Moon",
                "traits": ["Nurturing", "Intuitive", "Emotional"],
                "favorable_times": ["Night", "Summer"]
            },
            "Leo": {
                "element": "Fire",
                "quality": "Fixed",
                "ruler": "Sun",
                "traits": ["Creative", "Generous", "Charismatic"],
                "favorable_times": ["Daytime", "Summer"]
            },
            "Virgo": {
                "element": "Earth",
                "quality": "Mutable",
                "ruler": "Mercury",
                "traits": ["Analytical", "Practical", "Diligent"],
                "favorable_times": ["Morning", "Late Summer"]
            },
            "Libra": {
                "element": "Air",
                "quality": "Cardinal",
                "ruler": "Venus",
                "traits": ["Diplomatic", "Harmonious", "Fair"],
                "favorable_times": ["Evening", "Fall"]
            },
            "Scorpio": {
                "element": "Water",
                "quality": "Fixed",
                "ruler": "Pluto",
                "traits": ["Intense", "Passionate", "Strategic"],
                "favorable_times": ["Night", "Fall"]
            },
            "Sagittarius": {
                "element": "Fire",
                "quality": "Mutable",
                "ruler": "Jupiter",
                "traits": ["Optimistic", "Adventurous", "Philosophical"],
                "favorable_times": ["Morning", "Late Fall"]
            },
            "Capricorn": {
                "element": "Earth",
                "quality": "Cardinal",
                "ruler": "Saturn",
                "traits": ["Ambitious", "Disciplined", "Patient"],
                "favorable_times": ["Morning", "Winter"]
            },
            "Aquarius": {
                "element": "Air",
                "quality": "Fixed",
                "ruler": "Uranus",
                "traits": ["Innovative", "Independent", "Humanitarian"],
                "favorable_times": ["Afternoon", "Winter"]
            },
            "Pisces": {
                "element": "Water",
                "quality": "Mutable",
                "ruler": "Neptune",
                "traits": ["Compassionate", "Artistic", "Intuitive"],
                "favorable_times": ["Evening", "Late Winter"]
            }
        }
        
        # Determine zodiac sign based on birth date
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            sign = "Aquarius"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            sign = "Pisces"
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            sign = "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            sign = "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            sign = "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            sign = "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            sign = "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            sign = "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            sign = "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            sign = "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            sign = "Sagittarius"
        else:
            sign = "Capricorn"
            
        return {"sign": sign, **zodiac_info[sign]}

    def generate_horoscope_predictions(self, sign_data):
        """Generate personalized horoscope predictions based on sign characteristics"""
        element = sign_data["element"]
        traits = sign_data["traits"]
        favorable_times = sign_data["favorable_times"]
        
        predictions = {
            "daily": f"Your {element} element is particularly strong today. Focus on your {traits[0].lower()} nature to overcome challenges.",
            "weekly": f"This week, your {traits[1].lower()} qualities will help you succeed. {favorable_times[0]} hours will be most productive.",
            "monthly": f"This month brings opportunities to develop your {traits[2].lower()} side. Pay attention to opportunities during {favorable_times[1]}.",
            "yearly": f"This year emphasizes your connection with the {element} element. Your ruling planet {sign_data['ruler']} brings positive changes."
        }
        return predictions

    def calculate_lucky_elements(self, sign_data):
        """Calculate lucky elements based on zodiac sign"""
        element = sign_data["element"]
        
        # Define lucky colors based on element
        element_colors = {
            "Fire": ["Red", "Orange", "Gold"],
            "Earth": ["Green", "Brown", "Yellow"],
            "Air": ["Blue", "White", "Gray"],
            "Water": ["Blue", "Purple", "Silver"]
        }
        
        # Calculate lucky number based on ruling planet
        ruler_number = len(sign_data["ruler"]) % 9 + 1
        
        # Define lucky days based on quality
        quality_days = {
            "Cardinal": ["Monday", "Wednesday"],
            "Fixed": ["Tuesday", "Thursday"],
            "Mutable": ["Friday", "Sunday"]
        }
        
        return {
            "colors": element_colors[element],
            "number": ruler_number,
            "days": quality_days[sign_data["quality"]]
        }

    def get_detailed_horoscope(self):
        """Get detailed horoscope reading"""
        western = self.calculate_western_zodiac()
        predictions = self.generate_horoscope_predictions(western)
        lucky_elements = self.calculate_lucky_elements(western)
        
        return {
            "western": {
                "sign": western["sign"],
                "element": western["element"],
                "quality": western["quality"],
                "ruler": western["ruler"],
                "traits": western["traits"],
                "favorable_times": western["favorable_times"],
                "predictions": predictions
            },
            "lucky": lucky_elements
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        name = request.form.get('name', '')
        dob = request.form.get('dob', '')
        time = request.form.get('time', '')
        lat = float(request.form.get('latitude', 0))
        lon = float(request.form.get('longitude', 0))

        # Calculate astrological details
        calculator = AstrologyCalculator(dob, time, lat, lon)
        horoscope_data = calculator.get_detailed_horoscope()
        
        # Get birth period
        birth_datetime = datetime.strptime(f"{dob} {time}", "%Y-%m-%d %H:%M")
        birth_hour = birth_datetime.hour
        
        if 5 <= birth_hour < 12:
            period = "morning person"
        elif 12 <= birth_hour < 17:
            period = "afternoon person"
        else:
            period = "night person"

        return render_template('result.html',
                           name=name,
                           horoscope=horoscope_data,
                           birth_period=period)
    
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)