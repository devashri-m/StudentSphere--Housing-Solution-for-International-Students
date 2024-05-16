
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from apps.apartments.models import Apartment  


class GetCommentsAPIView(APIView):
    def get(self, request, apartment_id):
        try:
            comments = Comment.objects.filter(apartment_id=apartment_id)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        except Apartment.DoesNotExist:
            return Response({"error": "Apartment not found."}, status=status.HTTP_404_NOT_FOUND)



    
class AddCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the authenticated student's ID
        student_id = request.user.id

        request.data['student_id'] = student_id
        request.data['apartment_id'] = self.kwargs['apartment_id']

        print("Request Data:", request.data)  # Debug

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Serializer Errors:", serializer.errors)  # Debug
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        
        print("Comment Author ID:", comment.student.id)
        print("Request User ID:", request.user.id)
        
        if comment.student.id != request.user.id:
            return Response({"error": "You are not authorized to delete this comment."}, status=status.HTTP_403_FORBIDDEN)
        
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EditCommentAPIView(APIView):
        permission_classes = [IsAuthenticated]

        def put(self, request, comment_id):
            try:
                comment = Comment.objects.get(id=comment_id)
            except Comment.DoesNotExist:
                return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)

            if comment.student.id != request.user.id:
                return Response({"error": "You are not authorized to edit this comment."}, status=status.HTTP_403_FORBIDDEN)

            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

