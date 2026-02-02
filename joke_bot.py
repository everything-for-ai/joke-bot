#!/usr/bin/env python3
"""
Joke Bot - Daily jokes and fun facts delivery
Supports multiple platforms: Feishu, WeCom, Telegram, etc.
"""

import os
import json
import random
from typing import Dict, List


class JokeBot:
    def __init__(self, config_file: str = "config.json"):
        self.config = self.load_config(config_file)
        self.jokes = self.load_jokes()
    
    def load_config(self, config_file: str) -> Dict:
        """Load configuration"""
        default_config = {
            "schedule": "12:00",
            "platforms": ["feishu"],
            "joke_types": ["chinese", "english", "pun", "code"]
        }
        
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
                default_config.update(config)
        
        return default_config
    
    def load_jokes(self) -> Dict[str, List[str]]:
        """Load joke database"""
        return {
            "chinese": [
                "为什么程序员喜欢黑色？因为 RGB(0,0,0) 是黑色的！",
                "程序员最讨厌的饼：画的饼",
                "代码写完了，测试是不可能测试的，这辈子都不可能测试的。",
                "两个程序员结婚，生个孩子叫字节，女儿叫字节跳不动。",
                "程序员的双肩包里面永远是电脑、充电器、还有咖啡。"
            ],
            "english": [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "There's no place like 127.0.0.1",
                "Software and beer: both free, both open source, both make you feel weird without.",
                "Why do Java developers wear glasses? Because they can't C#!",
                "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?'"
            ],
            "pun": [
                "The computer was always lying to me, it had a hard disk and a chip on its shoulder.",
                "I told my computer I needed a break, now it won't stop sending me vacation ads.",
                "Programmers are gearheads for the mind, debugging is just mental auto repair.",
                "My code doesn't have bugs, it just develops unexpected features."
            ],
            "code": [
                "// This code is perfect until you try to understand it",
                "TODO: Fix this later (never)",
                "if (it works) { don't touch it; } // The golden rule",
                "// I wrote this code, but God knows what it does",
                "print('Hello, World!') // The beginning of every programmer's journey"
            ]
        }
    
    def get_random_joke(self, types: List[str] = None) -> str:
        """Get a random joke"""
        if types is None:
            types = self.config.get("joke_types", ["chinese", "english"])
        
        all_jokes = []
        for joke_type in types:
            if joke_type in self.jokes:
                all_jokes.extend(self.jokes[joke_type])
        
        if not all_jokes:
            all_jokes = self.jokes["chinese"]
        
        return random.choice(all_jokes)
    
    def get_daily_jokes(self, count: int = 3) -> str:
        """Get multiple jokes for daily delivery"""
        jokes = []
        for i in range(count):
            joke = self.get_random_joke()
            jokes.append(f"{i+1}. {joke}")
        
        return f"""
😄 每日一笑 - {jokes[0].split('.')[0]}

{chr(10).join(jokes)}

#笑话 #每日一笑 #开心一笑
        """.strip()
    
    def send_to_feishu(self, message: str):
        """Send to Feishu"""
        print(f"[Feishu] {message}")
    
    def send_to_wecom(self, message: str):
        """Send to WeCom"""
        print(f"[WeCom] {message}")
    
    def run(self):
        """Main execution"""
        message = self.get_daily_jokes()
        print(message)
        return message


if __name__ == "__main__":
    bot = JokeBot()
    bot.run()
