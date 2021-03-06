import hashlib
import binascii


class fileinfo:
	def __init__(self, file):
		self.file = file
		self.file_buf = file.read()


	def get_md5(self):
		try:
			md5 = hashlib.md5()
			md5.update(self.file_buf)
			return md5.hexdigest().upper()
		except:
			return None


	def get_crc32(self):
            crc = binascii.crc32(self.file_buf)
            if crc >= 0:
                crc = "%X" %crc
                crc = "%s%s" %((8 - len(crc)) * '0', crc)
                return crc
            else:
                crc = "%X" %(~crc ^ 0xffffffff)
                crc = "%s%s" %((8 - len(crc)) * '0', crc)

                return crc


	def get_sha256(self):
		sha256 = hashlib.sha256()
		sha256.update(self.file_buf)
		return sha256.hexdigest().upper()


	def get_sha1(self):
		sha1 = hashlib.sha1()
		sha1.update(self.file_buf)
		return sha1.hexdigest().upper()


	def get_len(self):
		return len(self.file_buf)


	def get_name(self):
		return self.file.filename


	def get_type(self):
		return "unknown"


	def get_buf(self):
		return self.file_buf


	def get_size(self):
		file_size = len(self.file_buf)
		if file_size < 1024:
			return str(file_size) + 'B'
		elif 1024 < file_size < 1024 * 1024:
			return str(file_size / 1024) + 'KB'
		elif 1024 * 1024 < file_size < 1024 * 1024 * 1024:
			return str(round(float(file_size) / (1024 * 1024), 2)) + 'MB'


	def get_fileinfo(self):
		file_feature = {}
		file_feature['name'] = self.get_name()
		file_feature['md5'] = self.get_md5()
		file_feature['sha1'] = self.get_sha1()
		file_feature['crc'] = self.get_crc32()
		return file_feature


def tell_analysis_procedure(steps):
    '''
    get the procedure of analysis 
    '''
    if isinstance(steps, list):
        procedure_desc = '|'.join(steps)
    elif isinstance(steps, dict):
        procedure_desc = '|'.join(steps['node_list'])
    return procedure_desc

