def analyze_user_activity(log_file_path: str) -> dict:
    #your code here
def analyze_user_activity(log_file_path: str) -> dict:
    #your code here
    action_counts = {}
    user_actions = {}
    session_times = []
    users = set()

    try:
        with open(log_file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()

                # ข้ามบรรทัดที่ข้อมูลไม่ครบหรือเกิน
                if len(parts) != 4:
                    continue

                timestamp, user_id, action, duration = parts

                # duration ต้องเป็นตัวเลข
                try:
                    duration = int(duration)
                except ValueError:
                    continue

                users.add(user_id)

                # นับจำนวน action
                action_counts[action] = action_counts.get(action, 0) + 1

                # นับ activity ของแต่ละ user
                user_actions[user_id] = user_actions.get(user_id, 0) + 1

                # เก็บเวลา session จาก login
                if action == "login":
                    session_times.append(duration)

    except (FileNotFoundError, OSError):
        return {
            "total_users": 0,
            "action_counts": {},
            "most_active_user": None,
            "average_session_time": 0.0
        }

    # หา user ที่มี activity มากที่สุด
    most_active_user = None
    if user_actions:
        most_active_user = max(
            user_actions,
            key=user_actions.get
        )

    # ค่าเฉลี่ย session time
    average_session_time = 0.0
    if session_times:
        average_session_time = sum(session_times) / len(session_times)

    return {
        "total_users": len(users),
        "action_counts": action_counts,
        "most_active_user": most_active_user,
        "average_session_time": average_session_time
    }


if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}


if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}
