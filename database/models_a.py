import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()


from django.db import models

class Report(models.Model):
    slug = models.CharField(max_length=36, unique=True)  # UUID format

    def __str__(self):
        return self.slug

class CreditScore(models.Model):
    status_id = models.IntegerField()
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=255)
    credit_bureau_id = models.IntegerField()
    credit_score = models.CharField(max_length=255)
    lender_rank = models.CharField(max_length=255, null=True, blank=True)
    score_scale = models.CharField(max_length=255, null=True, blank=True)
    type = models.IntegerField()
    report = models.ForeignKey(Report, related_name='credit_scores', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    old_scores = models.CharField(max_length=255)
    score_difference = models.CharField(max_length=255)
    credit_reporting_agency = models.JSONField()

    class Meta:
        indexes = [
            models.Index(fields=['report']),
            models.Index(fields=['user_id']),
        ]

    def __str__(self):
        return f"CreditScore {self.id} for Report {self.report_id}"

class Summary(models.Model):
    report = models.ForeignKey(Report, related_name='summaries', on_delete=models.CASCADE)
    credit_bureau_id = models.IntegerField()
    total_accounts = models.CharField(max_length=255)
    open_accounts = models.CharField(max_length=255)
    closed_accounts = models.CharField(max_length=255)
    collection = models.CharField(max_length=255, null=True, blank=True)
    delinquent = models.CharField(max_length=255)
    derogatory = models.CharField(max_length=255)
    balances = models.CharField(max_length=255)
    payments = models.CharField(max_length=255)
    public_records = models.CharField(max_length=255)
    inquiries = models.CharField(max_length=255)
    type = models.IntegerField()
    credit_reporting_agency = models.JSONField()

    class Meta:
        indexes = [
            models.Index(fields=['report']),
        ]

    def __str__(self):
        return f"Summary {self.id} for Report {self.report_id}"

class PersonalInformation(models.Model):
    report = models.ForeignKey(Report, related_name='personal_information', on_delete=models.CASCADE)
    credit_bureau_id = models.IntegerField()
    name = models.JSONField()
    dob = models.JSONField()
    aka_name = models.JSONField()
    former = models.CharField(max_length=255)
    current_addresses = models.JSONField()
    previous_addresses = models.JSONField()
    employers = models.JSONField()
    type = models.CharField(max_length=255)
    credit_reporting_agency = models.JSONField()

    class Meta:
        indexes = [
            models.Index(fields=['report']),
        ]

    def __str__(self):
        return f"PersonalInformation {self.id} for Report {self.report_id}"

class AccountHistory(models.Model):
    account_unique_id = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=255)
    credit_bureau_id = models.IntegerField()
    furnisher_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255)
    account_detail = models.CharField(max_length=255)
    bureau_code = models.CharField(max_length=255)
    account_status = models.CharField(max_length=255)
    monthly_payment = models.CharField(max_length=255)
    date_opened = models.CharField(max_length=255)
    balance = models.CharField(max_length=255)
    number_of_months = models.CharField(max_length=255)
    high_credit = models.CharField(max_length=255)
    credit_limit = models.CharField(max_length=255)
    past_due = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    late_status = models.CharField(max_length=255)
    last_reported = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    date_last_active = models.CharField(max_length=255)
    date_last_payment = models.CharField(max_length=255)
    payment_history = models.JSONField()
    type = models.IntegerField()
    report = models.ForeignKey(Report, related_name='account_histories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.IntegerField(null=True, blank=True)
    contacted = models.IntegerField()
    account_history_id = models.IntegerField(null=True, blank=True)
    bureau_dispute_status = models.IntegerField(null=True, blank=True)
    creditor_dispute_status = models.IntegerField(null=True, blank=True)
    text = models.CharField(max_length=255)
    class_type = models.CharField(max_length=255)
    credit_contact = models.JSONField()

    class Meta:
        indexes = [
            models.Index(fields=['report']),
            models.Index(fields=['user_id']),
        ]

    def __str__(self):
        return f"AccountHistory {self.id} for Report {self.report_id}"

class Inquiry(models.Model):
    creditor_name = models.CharField(max_length=255)
    type_of_business = models.CharField(max_length=255)
    date_of_inquiry = models.CharField(max_length=255)
    credit_bureau = models.CharField(max_length=255)
    type = models.IntegerField()
    is_deleted = models.IntegerField(null=True, blank=True)
    account_history_id = models.IntegerField(null=True, blank=True)
    bureau_dispute_status = models.IntegerField()
    creditor_dispute_status = models.IntegerField()
    class_type = models.CharField(max_length=255)
    account_history = models.JSONField(null=True, blank=True)
    credit_contact = models.JSONField()
    report = models.ForeignKey(Report, related_name='inquiries', on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['report']),
        ]

    def __str__(self):
        return f"Inquiry {self.id} for Report {self.report_id}"

class CreditContact(models.Model):
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=255)
    creditor_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255, null=True, blank=True)
    type = models.IntegerField()
    report = models.ForeignKey(Report, related_name='credit_contacts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    contacted = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['report']),
            models.Index(fields=['user_id']),
        ]

    def __str__(self):
        return f"CreditContact {self.id} for Report {self.report_id}"

class DataFurnisher(models.Model):
    report = models.ForeignKey(Report, related_name='data_furnishers', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    state_abbrev = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    phone_number1 = models.CharField(max_length=255)
    phone_number2 = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    links = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)
    category_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_report_free = models.IntegerField()
    is_report_freeze = models.IntegerField()
    checkbox = models.IntegerField()
    selected_address = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        unique_together = ('id', 'report')
        indexes = [
            models.Index(fields=['report']),
        ]

    def __str__(self):
        return f"DataFurnisher {self.id} for Report {self.report_id}"
