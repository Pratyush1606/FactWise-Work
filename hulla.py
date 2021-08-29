import os
for dname, dirs, files in os.walk("Factwise-Backend/scripts_for_purchase_order_data_upload"):
	for fname in files:
		if("pyc" in fname):
			continue
		fpath = os.path.join(dname, fname)
		with open(fpath) as f:
		    s = f.read()
		s = s.replace("localhost", "127.0.0.1")
		with open(fpath, "w") as f:
		    f.write(s)