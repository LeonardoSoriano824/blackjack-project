from pydealer import Card
from project import compare_points, convert_rank, convert_suit, rank_sum
from pyfiglet import Figlet


f = Figlet(font="larry3d")

def test_convert_rank():
    assert convert_rank("Ace") == "A"
    assert convert_rank("King") == "K"
    assert convert_rank("Queen") == "Q"
    assert convert_rank("Jack") == "J"
    assert convert_rank("2") == "2"
    assert convert_rank("3") == "3"
    assert convert_rank("4") == "4"
    assert convert_rank("5") == "5"
    assert convert_rank("6") == "6"
    assert convert_rank("7") == "7"
    assert convert_rank("8") == "8"
    assert convert_rank("9") == "9"
    assert convert_rank("10") == "10"

def test_convert_suit():
    assert convert_suit("Diamonds") == "♦"
    assert convert_suit("Hearts") == "♥"
    assert convert_suit("Spades") == "♠"
    assert convert_suit("Clubs") == "♣"

def test_compare_points():
    assert compare_points(21, 20) == f.renderText("You win!")
    assert compare_points(20, 21) == f.renderText("Dealer wins!")
    assert compare_points(20, 20) == f.renderText("It's a draw!")

def test_rank_sum():
    assert rank_sum([Card("2", "hearts"), Card("3", "hearts"), Card("4", "hearts")]) == 9
    assert rank_sum([Card("Ace", "hearts"), Card("Ace", "clubs"), Card("Ace", "Spades")]) == 13
    assert rank_sum([Card("Ace", "Hearts"), Card("King", "clubs"), Card("9", "Spades")]) == 20
    assert rank_sum([Card("Ace", "hearts"), Card("King", "hearts")]) == 21
    assert rank_sum([Card("Jack", "hearts"), Card("King", "hearts")]) == 20
    assert rank_sum([Card("2", "hearts"), Card("3", "hearts")]) == 5
    assert rank_sum([Card("10", "hearts"), Card("Ace", "hearts"), Card("King", "hearts"), Card("10", "Spades")]) == 31