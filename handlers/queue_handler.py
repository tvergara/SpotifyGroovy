from handlers.base import BaseHandler

class QueueHandler(BaseHandler):
    def pattern(self):
        return r'-q(ueue)?\s(.*)$'
      
    def handle(self):
        video_id = self.yt_search(self.match.group(2))
        self.yt.add_to_queue(video_id)
        self.acknowledge()
