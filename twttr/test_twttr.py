from twttr import shorten

def main():
    
    pass

def test_shorten():

    try:

        assert shorten('seven') == 'svn'

    except AssertionError:

        print("seven was not svn")

if __name__=='__main__':

    main()
