from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserModelForm, UserProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


@login_required
def users_profile(request, user_id):

    # get user object
    logged_in_user = get_object_or_404(User, id=user_id)

    # If the logged in user is the same as the user whose profile is being viewed,
    if request.user.id == user_id == logged_in_user.id:
        if request.method == 'POST':
            user_form = UserModelForm(request.POST, instance=request.user)
            profile_form = UserProfileForm(
                request.POST, instance=request.user.userprofilemodel)

            # If the form is valid, save the data and redirect to the profile page
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('users_profile', user_id=user_id)
        else:
            # If the request method is not POST, create a form with user data
            user_form = UserModelForm(instance=request.user)
            profile_form = UserProfileForm(instance=request.user.userprofilemodel)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'users_management/user_profile.html', context)
