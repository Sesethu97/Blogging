def check_has_user_voted(model, user, post):
    """
    Checks if request.user has voted. Returns Boolean.
    """
    try:
        model.objects.get(user=user, post=post)
        return True

    except model.DoesNotExist:
        return False


def cast_vote(post, vote_value, vote):
    """
    Creates new `Vote` object
    """
    vote.has_voted = True
    # Upvote
    if vote_value == 1:
        vote.value = vote_value
        post.upvotes = post.upvotes + 1
        post.save()
        vote.save()
    # Downvote
    elif vote_value == -1:
        vote.value = vote_value
        post.downvotes = post.downvotes + 1
        post.save()
        vote.save()
    # Cancel vote
    elif vote_value == 0:
        # If user previously downvoted the post
        if vote.value == -1:
            vote.value = 0
            post.downvotes = post.downvotes - 1
            post.save()
            vote.save()

        # If user previously upvoted the post
        elif vote.value == 1:
            vote.value = 0
            post.upvotes = post.upvotes - 1
            post.save()
            vote.save()
        elif vote.value == 0:
            pass
