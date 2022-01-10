from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="pls send of the video", required=True)
video_put_args.add_argument("views", type=int, help="pls send of the views", required=True)
video_put_args.add_argument("likes", type=int, help="pls send of the likes", required=True)

update_video_put_args = reqparse.RequestParser()
update_video_put_args.add_argument("name", type=str, help="pls send of the video", )
update_video_put_args.add_argument("views", type=int, help="pls send of the views", )
update_video_put_args.add_argument("likes", type=int, help="pls send of the likes", )
videos = {}


def abort_if_video_not_found(video_id):
    if video_id not in videos:
        abort(404, message="Sorry Video Not Found")
def abort_if_video_found(video_id):
    if video_id in videos:
        abort(409, message="Pls check the id with already exists")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_not_found(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_found(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return {"video": args}

    def delete(self, video_id):
        abort_if_video_not_found(video_id)
        del videos[video_id]
        return '',204
    def patch(self, video_id):
        abort_if_video_not_found(video_id)
        args = update_video_put_args.parse_args()
        for i in args:
            if args[i] != None:
                videos[video_id][i] = args[i]
api.add_resource(Video, "/video/<int:video_id>")
if __name__ == "__main__":
    app.run(debug=True)
