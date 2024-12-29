import mariadb
import math
import string
import sys

def read_db(cur, id_no):
    
    sql = "SELECT data FROM essay WHERE id=%s"
    choose = (id_no,)
    cur.execute(sql, choose)
    data = cur.fetchone()	
    if not data:
        raise ValueError('no results for required query')
    return data[0]


def get_words_from_line_list(text):
    
    translation_table = str.maketrans(string.punctuation+string.ascii_uppercase, " "*len(string.punctuation)+string.ascii_lowercase)
    text = text.translate(translation_table)
    word_list = text.split()
    
    return word_list


def count_frequency(word_list):
    
    D = {}
    
    for new_word in word_list:
        
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    
    return D


def word_frequencies_for_db(cur,id_no):
    
    line_list = read_db(cur,id_no)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    
    print("DB", id_no, ":", )
    print(len(line_list), "lines", )
    print(len(word_list), "words", )
    print(len(freq_mapping), "distinct words")
    
    return freq_mapping


def multiplyProduct(D1, D2):
    
    Sum = 0.0
    
    for key in D1:
        
        if key in D2:
            Sum += (D1[key] * D2[key])
    
    return Sum


def vector_angle(D1, D2):
    
    numerator = multiplyProduct(D1, D2)
    denominator = math.sqrt(multiplyProduct(D1,D1)*multiplyProduct(D2,D2))
    
    return math.acos(numerator / denominator)


def documentSimilarity(cur,id_no_1,id_no_2):
    
    sorted_word_list_1 = word_frequencies_for_db(cur,id_no_1)
    sorted_word_list_2 = word_frequencies_for_db(cur,id_no_2)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
    
    print("Result nearer to a zero - exactly similar", )
    print("Result nearer to an one - opposite", )
    print("The distance between data is: % 0.6f (radians)"% distance)


def print_data(cur):

	results = []

	cur.execute("SELECT id, author, data FROM essay")

	for (id, author, data) in cur:
		results.append(f"{id} {author} {data}")

	print("\n".join(results))


try:
	conn = mariadb.connect(
		host = 'localhost', 
		port = 3306,
		user = 'pydb',
		password = 'pypass',
		database = 'test')
	
	cur = conn.cursor()

	print_data(cur)
	print("")
	if(len(sys.argv) < 2):
            raise ValueError('first argument is not set')
	if(len(sys.argv) < 3):
            raise ValueError('second argument is not set')
	documentSimilarity(cur,sys.argv[1], sys.argv[2])

	conn.close()

except mariadb.Error as e:
	print(f"Error connecting to the database: {e}")
	sys.exit(1)
