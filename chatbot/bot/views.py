import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from groq import Groq

API_KEY = os.environ.get('GROQ_API_KEY')
if not API_KEY:
    raise RuntimeError('Missing GROQ_API_KEY in environment. Set it in .env')
client = Groq(api_key=API_KEY)


def cors_json_response(data, status=200):
    response = JsonResponse(data, status=status)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    return response


@csrf_exempt
@require_http_methods(['POST', 'OPTIONS'])
def chat_bot(request):
    if request.method == 'OPTIONS':
        response = JsonResponse({'status': 'ok'})
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    try:
        body = json.loads(request.body.decode('utf-8') or '{}')
    except json.JSONDecodeError:
        return cors_json_response({'error': 'Invalid JSON'}, status=400)

    user_message = body.get('message', '').strip()
    if not user_message:
        return cors_json_response({'error': 'No message provided'}, status=400)

   
    

    try:
        response = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[{'role': 'system', 'content': "you are advance ai named Parash gpt and your creator is parash khadka mensioned these details when asked otherwise do not mensioned this"},{'role': 'user', 'content': user_message}],
        )
        reply = response.choices[0].message.content
        return cors_json_response({'reply': reply})
    except Exception as exc:
        return cors_json_response(
            {'error': 'Unable to generate a response', 'details': str(exc)},
            status=500,
        )
