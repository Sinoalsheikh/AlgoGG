import unittest
from lvlhub.src.core import LvlhubPlatform, SuiteType

class TestLvlhubPlatform(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.platform = LvlhubPlatform()
        self.test_user_id = "test_user"
        self.test_auth_data = {
            "username": "test_user",
            "password": "secure_password"
        }

    def test_create_session(self):
        """Test session creation"""
        session_token = self.platform.create_session(self.test_user_id, self.test_auth_data)
        self.assertIsNotNone(session_token)
        self.assertIn(session_token, self.platform.active_sessions)

    def test_process_request(self):
        """Test request processing"""
        # Create session first
        session_token = self.platform.create_session(self.test_user_id, self.test_auth_data)
        
        # Test recommendation request
        request_data = {
            "type": "recommendation",
            "parameters": {
                "context": "work",
                "limit": 5
            }
        }
        recommendations = self.platform.process_request(session_token, request_data)
        self.assertIsInstance(recommendations, list)

    def test_user_profile_creation(self):
        """Test user profile creation"""
        demographics = {"industry": "technology", "company_size": "500+"}
        preferences = {"theme": "dark", "notifications": True}
        
        profile = self.platform.core.create_user_profile(
            user_id=self.test_user_id,
            suite_type=SuiteType.ENTERPRISE,
            demographics=demographics,
            preferences=preferences
        )
        
        self.assertEqual(profile.user_id, self.test_user_id)
        self.assertEqual(profile.suite_type, SuiteType.ENTERPRISE)
        self.assertEqual(profile.demographics, demographics)
        self.assertEqual(profile.preferences, preferences)

if __name__ == '__main__':
    unittest.main()
