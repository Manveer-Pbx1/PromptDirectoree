import pytest
import mongomock
from django.test import TestCase, Client
from unittest.mock import patch, MagicMock
from bson import ObjectId
from datetime import datetime
import os
import django


def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'promptDirectory.settings')
    django.setup()

@pytest.fixture
def mock_mongo_client():
    """Fixture to provide a mocked MongoDB client"""
    with patch('pymongo.MongoClient') as mock_client:
        mock_db = mongomock.MongoClient().db
        mock_client.return_value = MagicMock()
        mock_client.return_value.__getitem__.return_value = mock_db
        yield mock_client


@pytest.fixture
def mock_mongo_collection():
    """Fixture to provide a mocked MongoDB collection"""
    collection = mongomock.MongoClient().db.collection
    return collection


@pytest.fixture
def sample_prompt_data():
    """Fixture providing sample prompt data"""
    return {
        "title": "Test Prompt",
        "content": "Generate a creative story about...",
        "category": "creative",
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }


@pytest.fixture
def sample_prompt_with_id():
    """Fixture providing sample prompt data with MongoDB ObjectId"""
    return {
        "_id": ObjectId("507f1f77bcf86cd799439011"),
        "title": "Test Prompt",
        "content": "Generate a creative story about...",
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }


@pytest.fixture
def multiple_prompts():
    """Fixture providing multiple sample prompts"""
    return [
        {
            "_id": ObjectId("507f1f77bcf86cd799439011"),
            "title": "Creative Writing Prompt",
            "content": "Write a story about a magical forest",
        },
        {
            "_id": ObjectId("507f1f77bcf86cd799439012"), 
            "title": "Code Review Prompt",
            "content": "Review this Python code for best practices",
        },
        {
            "_id": ObjectId("507f1f77bcf86cd799439013"),
            "title": "Business Analysis Prompt", 
            "content": "Analyze the market trends for...",
        }
    ]


@pytest.fixture
def invalid_prompt_data():
    """Fixture providing invalid prompt data for testing validation"""
    return {
        "title": "A"*1000, 
        "content": "",  
    }


@pytest.fixture 
def api_client():
    """Fixture providing Django test client"""
    return Client()


@pytest.fixture(scope="session")
def test_mongo_settings():
    """Test MongoDB settings"""
    return {
        'host': 'localhost',
        'port': 27017,
        'database': 'promptDirectory',
        'collection': 'prompts'
    }