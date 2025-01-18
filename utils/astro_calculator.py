import swisseph as swe
from datetime import datetime
import pytz
import math

class AstroCalculator:
    def __init__(self):
        # Set ephemeris path
        swe.set_ephe_path()
        
        # Define planets
        self.planets = {
            swe.SUN: "Sun",
            swe.MOON: "Moon",
            swe.MARS: "Mars",
            swe.MERCURY: "Mercury",
            swe.JUPITER: "Jupiter",
            swe.VENUS: "Venus",
            swe.SATURN: "Saturn",
            swe.MEAN_NODE: "Rahu",
            swe.TRUE_NODE: "Ketu"
        }
        
        # Define zodiac signs
        self.zodiac_signs = [
            "Aries", "Taurus", "Gemini", "Cancer",
            "Leo", "Virgo", "Libra", "Scorpio",
            "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ]
        
        # Define houses and their meanings
        self.house_meanings = {
            1: "Self, personality, physical appearance",
            2: "Wealth, family, speech",
            3: "Siblings, courage, communication",
            4: "Mother, emotions, home, property",
            5: "Children, intelligence, creative pursuits",
            6: "Enemies, diseases, debts, service",
            7: "Marriage, business partnerships, relationships",
            8: "Longevity, obstacles, hidden aspects",
            9: "Fortune, higher learning, spirituality",
            10: "Career, status, father",
            11: "Gains, aspirations, elder siblings",
            12: "Losses, expenses, spirituality, foreign travels"
        }

    def calculate_birth_chart(self, birth_data):
        """Calculate birth chart details"""
        try:
            # Convert birth time to Julian day
            birth_dt = datetime.strptime(f"{birth_data['date']} {birth_data['time']}", 
                                       "%Y-%m-%d %H:%M")
            timezone = pytz.timezone(birth_data['timezone'])
            birth_dt = timezone.localize(birth_dt)
            jul_day = swe.julday(birth_dt.year, birth_dt.month, birth_dt.day,
                               birth_dt.hour + birth_dt.minute/60.0)
            
            # Calculate Ascendant
            asc = swe.houses(jul_day, birth_data['lat'], birth_data['lon'])[1][0]
            ascendant_sign = self.get_zodiac_sign(asc)
            
            # Calculate planet positions
            planet_positions = {}
            for planet_id in self.planets:
                position = swe.calc_ut(jul_day, planet_id)[0]
                sign = self.get_zodiac_sign(position[0])
                planet_positions[self.planets[planet_id]] = {
                    'sign': sign,
                    'degree': position[0] % 30
                }
            
            # Calculate houses
            houses = swe.houses(jul_day, birth_data['lat'], birth_data['lon'])[0]
            house_signs = {i+1: self.get_zodiac_sign(house) 
                         for i, house in enumerate(houses)}
            
            return {
                'ascendant': ascendant_sign,
                'planets': planet_positions,
                'houses': house_signs
            }
            
        except Exception as e:
            raise Exception(f"Error calculating birth chart: {str(e)}")

    def get_zodiac_sign(self, degree):
        """Convert degree to zodiac sign"""
        sign_num = int(degree / 30)
        return self.zodiac_signs[sign_num]

    def generate_predictions(self, birth_chart):
        """Generate predictions based on birth chart"""
        predictions = {
            'personality': self._analyze_first_house(birth_chart),
            'career': self._analyze_career_houses(birth_chart),
            'relationships': self._analyze_relationship_houses(birth_chart),
            'health': self._analyze_health_houses(birth_chart),
            'finance': self._analyze_finance_houses(birth_chart),
            'spiritual': self._analyze_spiritual_houses(birth_chart)
        }
        return predictions

    def _analyze_first_house(self, birth_chart):
        """Analyze first house for personality traits"""
        ascendant = birth_chart['ascendant']
        personality_traits = {
            'Aries': "Natural leader, energetic, and confident",
            'Taurus': "Reliable, patient, and practical",
            'Gemini': "Versatile, intellectual, and communicative",
            'Cancer': "Nurturing, emotional, and protective",
            'Leo': "Charismatic, generous, and proud",
            'Virgo': "Analytical, modest, and hardworking",
            'Libra': "Diplomatic, charming, and harmonious",
            'Scorpio': "Intense, powerful, and mysterious",
            'Sagittarius': "Optimistic, adventurous, and philosophical",
            'Capricorn': "Ambitious, disciplined, and responsible",
            'Aquarius': "Independent, humanitarian, and innovative",
            'Pisces': "Compassionate, artistic, and intuitive"
        }
        return personality_traits.get(ascendant, "Balanced and adaptable personality")

    def _analyze_career_houses(self, birth_chart):
        """Analyze houses related to career (2nd, 6th, 10th)"""
        # Add career analysis logic here
        return "Your career path shows promise. Focus on your natural talents."

    def _analyze_relationship_houses(self, birth_chart):
        """Analyze houses related to relationships (5th, 7th)"""
        # Add relationship analysis logic here
        return "Relationships will play a significant role in your personal growth."

    def _analyze_health_houses(self, birth_chart):
        """Analyze houses related to health (1st, 6th, 8th)"""
        # Add health analysis logic here
        return "Maintain balance in your lifestyle for optimal health."

    def _analyze_finance_houses(self, birth_chart):
        """Analyze houses related to finance (2nd, 11th)"""
        # Add financial analysis logic here
        return "Financial prosperity comes through disciplined efforts."

    def _analyze_spiritual_houses(self, birth_chart):
        """Analyze houses related to spirituality (9th, 12th)"""
        # Add spiritual analysis logic here
        return "Your spiritual journey will lead to profound insights."