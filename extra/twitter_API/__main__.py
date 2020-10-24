from pyfiglet import Figlet

from classmodule import TwitterStreamer, StdOutListener

def main():
    f = Figlet(font='slant')
    print(f.renderText('TwitterStreamer \n By\n Felipe\tJonas\n'))
    print('\n.'*10) 

    hash_tag_list = ["Eleições"]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

if __name__ == '__main__':
    main()