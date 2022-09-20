from flask import Flask, url_for, send_from_directory, request
import logging, os
from werkzeug import secure_filename
from flask import render_template
from random import randint

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(static_file_dir)
# UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# RESULT_IMAGES = os.path.join(PROJECT_HOME, "results/swapimage.jpg")



def create_new_folder(local_dir):
	newpath = local_dir
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	print("add print")
	return newpath

@app.route('/')
def upload_file():
   return render_template("upload.html")

@app.route('/upload-file', methods = ['POST'])
def api_root():
	app.logger.info(UPLOAD_FOLDER)
	if request.method == 'POST':
		app.logger.info(app.config['UPLOAD_FOLDER'])
		img1 = request.files['image1']
		img2 = request.files['image2']

		img_name1 = secure_filename(img1.filename)
		img_name2 = secure_filename(img2.filename)
		create_new_folder(app.config['UPLOAD_FOLDER'])

		# print("Saving image file to server....")
		image_path1 = os.path.join(app.config['UPLOAD_FOLDER'], img_name1)
		app.logger.info("saving {}".format(image_path1))
		img1.save(image_path1)
		name=randint(0, 90000)

		RESULT_IMAGES = os.path.join(static_file_dir, "results/"+ str(name) +".jpg")
		image_path2 = os.path.join(app.config['UPLOAD_FOLDER'], img_name2)
		RESULT_URL = "http://192.168.23.189:8087/static/results/"+str(name)+".jpg"

		app.logger.info("saving {}".format(image_path2))
		img2.save(image_path2)

		# print("saved data....")
		s= 'python main.py --src '+ image_path1 + ' --dst ' + image_path2 + ' --out ' + RESULT_IMAGES + ' --correct_color'
		os.system(s)
		# render_template("output.html")
		# run faceswap hear
		return render_template("output.html", img_url=RESULT_URL)
	else:
		return "Where is the image?"
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
