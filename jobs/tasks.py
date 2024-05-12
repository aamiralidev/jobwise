from celery import shared_task
from jobs.models import JobBoard
from jobs.tasks.extractors import LeverBaseJobExtractor, GreenHouseBaseJobExtractor, BreezyBaseJobExtractor, AshbyBAseJobExtractor

@shared_task
def update_lever_job_boards():
    boards = JobBoard.objects.all().filter(provider='lever')
    for board in boards:
        try:
            LeverBaseJobExtractor(board.identifier, board.board_url).extract()
        except:
            pass

@shared_task
def update_greenhouse_job_boards():
    boards = JobBoard.objects.all().filter(provider='greenhouse')
    for board in boards:
        try:
            GreenHouseBaseJobExtractor(board.identifier, board.board_url).extract()
        except:
            pass 

@shared_task
def update_breezy_job_boards():
    boards = JobBoard.objects.all().filter(provider='breezy')
    for board in boards:
        try:
            BreezyBaseJobExtractor(board.identifier, board.board_url).extract()
        except:
            pass 

@shared_task
def update_ashbyhq_job_boards():
    boards = JobBoard.objects.all().filter(provider='ashbyhq')
    for board in boards:
        try:
            AshbyBAseJobExtractor(board.identifier, board.board_url).extract()
        except:
            pass 
