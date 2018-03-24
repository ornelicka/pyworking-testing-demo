import pytest
import subprocess
import sys
import rps


def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True #běžná syntaxe 

def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True #vyhodnocujeme, že je ten výsledek přesně TRUE! 

def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True

def test_lizard_is_invalid_play():
    assert rps.is_valid_play('lizard') is False 

def test_spock_is_invalid_play():
    assert rps.is_valid_play('spock') is False

def test_random_play_is_valid():
    for _ in range(100):
        play = rps.random_play()
        assert rps.is_valid_play(play) # is True by to bylo navíc

def test_random_play_is_fairish():
    plays = [rps.random_play() for _ in range(1000)] 
    assert plays.count('rock') > 100
    assert plays.count('paper') > 100
    assert plays.count('scissors') > 100
    
def test_paper_beats_rock():
    assert rps.determine_game_result('paper', 'rock') == 'human'

def test_rock_beats_scissors():
    assert rps.determine_game_result('rock', 'scissors') == 'human'

def test_scissors_beats_paper():
    assert rps.determine_game_result('scissors', 'paper') == 'human'

def test_paper_beats_rock():
    assert rps.determine_game_result('rock', 'paper') == 'computer'

def test_rock_beats_scissors():
    assert rps.determine_game_result('scissors', 'rock') == 'computer'

def test_scissors_beats_paper():
    assert rps.determine_game_result('paper', 'scissors') == 'computer'

def test_paper_paper_tie():
    assert rps.determine_game_result('paper', 'paper') == 'tie'

def test_rock_rock_tie():
    assert rps.determine_game_result('rock', 'rock') == 'tie'

def test_scissors_scissors_tie():
    assert rps.determine_game_result('scissors', 'scissors') == 'tie'


def input_fake(fake):
    def input_fake_(prompt):
        print(prompt)
        return fake
    return input_fake_ #fce, co vrací další fci - vyrábí falešné podvrhy rock, scissors, paper
    
#integrační testy/ black box testing, kdy se neřeší, co je uvnitř, ale program jako celek - main() nemá vstupní argumenty, ani return; je založena na side efektech (tzv procedura)
#na zachycení výstupu, můžeme dodat pomocné printy

@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors', 'lizard'])

def test_whole_game(capsys, monkeypatch, play): #capsys/monkeypatch je fixture; není to fce; parametr play pro parametrické testování, aby se ten test provedl postupně pro rock, scissors, paper
    #monkeypatch.setattr('builtins.input', input_fake_rock) 
    rps.main(input =input_fake(play)) # dependecy injection je čistší než monkeypatching (je univerzální pro celý kód, DP zase platí pro konkrétní fci)
    out, err = capsys.readouterr() # přečti std výstup a st chybový výstup
    assert 'rock, paper or scissors?' in out
    assert ('computer wins' in out) or ('human wins' in out) or ('It is a tie' in out)

def run_app(input):
    cp = subprocess.run([sys.executable, 'rps.py'],
                    input = 'asdf\nrock' ,
                    encoding = 'utf-8',
                    stdout=subprocess.PIPE)
    return cp.stdout

def test_game_asks_again_if_wrong_input():
    assert run_app ('adsf\nrock').count('rock, paper or scissors?') == 2
