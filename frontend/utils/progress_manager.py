import json
from pathlib import Path
from datetime import datetime
import streamlit as st

class ProgressManager:
    def __init__(self):
        self.data_dir = Path(__file__).parent.parent / "data"
        self.data_dir.mkdir(exist_ok=True)
        self.progress_file = self.data_dir / "user_progress.json"
        self._ensure_progress_file()

    def _ensure_progress_file(self):
        """Create progress file if it doesn't exist"""
        if not self.progress_file.exists():
            initial_data = {"users": {}}
            self.progress_file.write_text(json.dumps(initial_data, indent=2))

    def _load_progress(self):
        """Load progress data from file"""
        return json.loads(self.progress_file.read_text())

    def _save_progress(self, data):
        """Save progress data to file"""
        self.progress_file.write_text(json.dumps(data, indent=2))

    def update_user_progress(self, username: str, topic: str, quiz_score: int):
        """Update user's progress for a topic"""
        data = self._load_progress()
        
        if username not in data["users"]:
            data["users"][username] = {
                "topics_completed": [],
                "study_streak": 1,
                "total_study_time": 0,
                "badges": [],
                "achievements": {
                    "topics_mastered": 0,
                    "quizzes_completed": 0,
                    "perfect_scores": 0
                }
            }

        user_data = data["users"][username]
        
        # Update topic progress
        topic_entry = {
            "topic": topic,
            "completed_at": datetime.now().isoformat(),
            "quiz_score": quiz_score,
            "attempts": 1
        }

        # Check if topic already exists
        topic_exists = False
        for t in user_data["topics_completed"]:
            if t["topic"] == topic:
                t["attempts"] += 1
                t["quiz_score"] = max(t["quiz_score"], quiz_score)
                t["completed_at"] = topic_entry["completed_at"]
                topic_exists = True
                break

        if not topic_exists:
            user_data["topics_completed"].append(topic_entry)

        # Update achievements
        achievements = user_data["achievements"]
        achievements["quizzes_completed"] += 1
        
        if quiz_score == 100:
            achievements["perfect_scores"] += 1
            
            # Add perfect score badge if first time
            if achievements["perfect_scores"] == 1:
                user_data["badges"].append({
                    "name": "Perfect Score",
                    "earned_at": datetime.now().isoformat(),
                    "description": "Achieved 100% on a quiz"
                })

        # Save updated data
        self._save_progress(data)
        return user_data

    def get_user_progress(self, username: str):
        """Get user's progress data"""
        data = self._load_progress()
        return data["users"].get(username, {
            "topics_completed": [],
            "study_streak": 0,
            "total_study_time": 0,
            "badges": [],
            "achievements": {
                "topics_mastered": 0,
                "quizzes_completed": 0,
                "perfect_scores": 0
            }
        })

    def get_user_stats(self, username: str):
        """Get user's statistics for dashboard"""
        progress = self.get_user_progress(username)
        
        return {
            "topics_completed": len(progress["topics_completed"]),
            "average_score": sum(t["quiz_score"] for t in progress["topics_completed"]) / 
                           len(progress["topics_completed"]) if progress["topics_completed"] else 0,
            "study_streak": progress["study_streak"],
            "badges_earned": len(progress["badges"]),
            "perfect_scores": progress["achievements"]["perfect_scores"]
        }