
import argparse
import flickrapi
import flickrapi.shorturl

if __name__ == '__main__' :

    api_key = None
    api_secret = None

    parser = argparse.ArgumentParser ()
    parser.add_argument('userid', help='The user ID of the flickr user to use')
    parser.add_argument('-s', '--size', default='h', )
    args = parser.parse_args ()

    try:
        with open('flickr.key') as f:
            api_key = f.readline().strip()
            api_secret = f.readline().strip()
    except:
        print 'Failed reading flickr.key'
        exit(1)

    try:
        flickr = flickrapi.FlickrAPI(api_key, api_secret)
    except flickrapi.exceptions.FlickrError:
        print 'Bad api key'
        exit(1)

    for photo in flickr.walk(
        user_id=args.userid,
        sort='date-taken-desc'
    ):
        url = 'https://farm{0}.staticflickr.com/{1}/{2}_{3}_{4}.jpg'.format (
            photo.attrib['farm'],
            photo.attrib['server'],
            photo.attrib['id'],
            photo.attrib['secret'],
            args.size
        )

        import pprint
        pprint.pprint(photo.attrib)
