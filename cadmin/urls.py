from django.conf.urls import include, url
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index/', views.IndexView.as_view()),
    path('add-user/', views.AddUserView.as_view(), name='add-user'),
    path('users/', views.UsersView.as_view(), name='users'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('recover/', views.RecoverView.as_view(), name='recover'),
    path('set-pw/', views.SetPWView.as_view(), name='set-pw'),
    path('revenue/', views.RevenueView.as_view(), name='revenue'),
    path('revenue-details/', views.RevenueDetailsView.as_view(), name='revenue-details'),
    path('rev-stats/', views.RevStatsView.as_view(), name='stats'),
    path('offers/', views.OffersView.as_view(), name='offers'),
    path('offer-details/', views.OfferDetailsView.as_view(), name='offer-details'),
    path('trades/', views.TradesView.as_view(), name='trades'),
    path('trade-details/', views.TradeDetailsView.as_view(), name='trade-details'),
    path('customers/', views.CustomersView.as_view(), name='customers'),
    path('customer-details/', views.CustomerDetailsView.as_view(), name='customer-details'),
    path('customer-suspend/', views.CustomerSuspend.as_view(), name='customer-suspend'),
    path('transactions/', views.TransactionsView.as_view(), name='transactions'),
    path('transaction-details/', views.TransactionDetailsView.as_view(), name='transaction-details'),
    path('escrows/', views.EscrowsView.as_view(), name='escrows'),
    path('escrow-details/', views.EscrowDetailsView.as_view(), name='escrow-details'),
    path('escrow-release/', views.EscrowRelease.as_view(), name='escrow-release'),
    path('escrow-cancel/', views.EscrowCancel.as_view(), name='escrow-cancel'),
    path('support-center/', views.SupportCenterView.as_view(), name='support-center'),
    path('ticket-details-dispute/', views.TicketDetailsDisputeView.as_view(), name='ticket-details-dispute'),
    path('ticket-details-no-dispute/', views.TicketDetailsNoDisputeView.as_view(), name='ticket-details-no-dispute'),
    path('id-verify-app/', views.IdVerifyAppView.as_view(), name='id-verify-app'),
    path('id-verify-app-details/', views.IdVerifyAppDetailsView.as_view(), name='id-verify-app-details'),
    path('id-verify-app-accept/', views.IdVerifyAppAccept.as_view(), name='id-verify-app-accept'),
    path('id-verify-app-reject/', views.IdVerifyAppReject.as_view(), name='id-verify-app-reject'),
    path('contact-form/', views.ContactFormView.as_view(), name='contact-form'),
    path('contact-form-details/', views.ContactFormDetailsView.as_view(), name='contact-form-details'),
    path('additional-pages/', views.AdditionalPagesView.as_view(), name='additional-pages'),
    path('additional-page-preview/', views.AdditionalPagePreviewView.as_view(), name='addtional-page-preview'),
    path('add-new-page/', views.AddNewPageView.as_view(), name='add-new-page'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('post-preview/', views.PostPreviewView.as_view(), name='post-preview'),
    path('add-new-post/', views.AddNewPostView.as_view(), name='add-new-post'),
    path('tags/', views.TagsView.as_view(), name='tags'),
    path('media-library/', views.MediaLibraryView.as_view(), name='media-library'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('last-login/', views.LastLoginView.as_view(), name='last-login'),
    path('flagged-posts/', views.FlaggedPostsView.as_view(), name='flagged-posts'),
    path('flagged-post-details/', views.FlaggedPostDetailsView.as_view(), name='flagged-post-details'),
    path('add-landing-page/', views.AddLandingPageView.as_view(), name='add-landing-page'),
    path('add-pers-link/', views.AddPersLinkView.as_view(), name='add-pers-link'),
    path('add-redirection-link/', views.AddRedirectionLinkView.as_view(), name='add-redirection-link'),
    path('documentations/', views.DocumentationsView.as_view(), name='documentations'),
    path('post-issue/', views.PostIssueView.as_view(), name='post-issue'),
    path('seo/', views.SeoView.as_view(), name='seo'),
    path('security-status/', views.SecurityStatusView.as_view(), name='security-status'),
    path('options/', views.OptionsView.as_view(), name='options'),
    path('options-router-blog/', views.OptionsRouterBlogView.as_view(), name='options'),
    path('options-router-forgot-password/', views.OptionsRouterForgotPasswordView.as_view(), name='options'),
    path('campaigns/', views.CampaignsView.as_view(), name='campaigns'),
    path('campaign-updated/', views.CampaignUpdatedView.as_view(), name='campaign-updated'),
    path('affiliates/', views.AffiliatesView.as_view(), name='affiliates'),
    path('add-new-affiliate/', views.AddNewAffiliateView.as_view(), name='add-new-affiliate'),
    path('reports/', views.ReportsView.as_view(), name='reports'),
    path('community-posts/', views.CommunityPostsView.as_view(), name='community-posts'),
    path('community-post-details/', views.CommunityPostDetailsView.as_view(), name='community-post-details'),
    path('community-post-rules/', views.CommunityPostRulesView.as_view(), name='community-post-rules'),
]
