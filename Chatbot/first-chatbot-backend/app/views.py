from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests

token1 = 'g.a000gAilj7h9gwRY8cGkeGH--0if2YuvP28M7pmS6jaX2oDCnR34WTQ_izUz7RA2nEl6TK5GmwACgYKAcQSAQASFQHGX2Mij0z2xLdEHAo7MfknPMHhvxoVAUF8yKr_eARNBFpjw8TE6xrOYDeF0076'
token2 = 'sidts-CjEBPVxjStWM0_9klzmgheAQsWLNlHFFlcET98GeFF6imbJWyXdNoaFiBnsNdoW5LYtoEAA'
token3 = 'ABTWhQHtg8wdhD1QFyb2rpp9O2EycswwQQC_ieJx-mxuP-GUEyWH5vcMiUHf-iBlk4BF3in3'

tokenCookies = {
    '__Secure-1PSID': token1,
    '__Secure-1PSIDTS': token2,
    '__Secure-1PSIDCC': token3
}

bard = BardCookies(cookie_dict=tokenCookies)

class ChatBotView(APIView):
    def post(self, request):
        data = request.data

        conversationId = data.get('conversationId')

        if conversationId is not None:
            bard.conversation_id = conversationId
        else:
            bard.conversation_id = None

        answer = bard.get_answer(data['question'])

        return Response(status=201, data=answer)