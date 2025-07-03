from datetime import datetime

def format_timestamp():
    return datetime.utcnow().strftime('%-d %B %Y - %-I:%M %p UTC')

def format_event(event_type, data):
    ts = format_timestamp()

    if event_type == "push":
        author = data["pusher"]["name"]
        branch = data["ref"].split("/")[-1]
        return f"{author} pushed to {branch} on {ts}"

    if event_type == "pull_request":
        pr = data["pull_request"]
        author = pr["user"]["login"]
        from_branch = pr["head"]["ref"]
        to_branch = pr["base"]["ref"]
        if data["action"] == "opened":
            return f"{author} submitted a pull request from {from_branch} to {to_branch} on {ts}"
        if data["action"] == "closed" and pr["merged"]:
            return f"{author} merged branch {from_branch} to {to_branch} on {ts}"

    return None
