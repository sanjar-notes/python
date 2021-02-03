import os

def intro():
    print('Nice to meet you, {}.'.format(input("I'm Lenovo fx15, you are: ")))

def capital(name='Name'):
    lambda name: name.capitalize()
    return name

def play_song():
    # print the list of available music
    os.chdir('/home/sanjar/Music/')
    song_list = os.listdir()
    song_list.sort()
    # return

    while True:
        # player starts
        print('Press Q to quit')
        for i in enumerate(song_list):
            print('\t{:>2}. {}'.format(i[0]+1, i[1][:-4]))
        try:
            selected_song = input('Select the song: ')
            if selected_song in ['Q', 'q', 'quit', 'exit','close']:
                print('Exiting the player...')
                break
            selected_song = int(input('Select the song: '))-1
            if 0 <= selected_song < len(song_list):
                os.system('mpv "{}"'.format(song_list[selected_song]))
        except ValueError:
            print('Invalid Input...')
            os.system('clear')

# the only change required
# run directly only if running as a script
if __name__ == '__main__':
    #driver
    play_song()
