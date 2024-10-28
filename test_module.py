import unittest
from demographic_data_analyzer import calculate_demographic_data

class DemographicAnalyzerTestCase(unittest.TestCase):
    def test_race_count(self):
        result = calculate_demographic_data()
        self.assertEqual(result['race_count'].iloc[0], 27816)  # Ejemplo: número de personas de la primera raza

    def test_average_age_men(self):
        result = calculate_demographic_data()
        self.assertEqual(result['average_age_men'], 39.4)

    def test_higher_education_rich(self):
        result = calculate_demographic_data()
        self.assertEqual(result['higher_education_rich'], 46.5)

if __name__ == "__main__":
    unittest.main()
