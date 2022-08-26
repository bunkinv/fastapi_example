import uvicorn

def main():
	# Run server
	uvicorn.run("app.app:app", host='0.0.0.0', port=8000,
	            reload=True, access_log=True, log_level='debug', use_colors=True)


if __name__ == '__main__':
	main()
