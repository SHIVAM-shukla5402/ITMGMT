from django.db import models
#from django.db import encrypted_fields


# Create your models here.
class Post_Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    type = models.ForeignKey(Post_Type,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    on_date = models.DateField()
    attachement = models.FileField(upload_to="data",null=True,blank=True)

    class Meta:
        verbose_name = "Post"

    def __str__(self):
        return self.title

class Department(models.Model):
    name = models.CharField(max_length=200)
    docstatus = models.CharField(max_length=1,null=True)
    disable = models.CharField(max_length=1,null=True)

    class Meta:
        verbose_name="Department"

    def __str__(self):
        return self.name

class User(models.Model):
    login = models.CharField(max_length=200)
   # password = encrypted_fields.EncryptedCharField(max_length=500)
    password = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.BigIntegerField(blank=True, null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    disable = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User Details"

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pincode = models.CharField(max_length=20)
    gstin = models.CharField(max_length=20)
    entry_date = models.DateTimeField(blank = True,null = True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Costcenter(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pincode = models.CharField(max_length=20)
    gstin = models.CharField(max_length=20)
    entry_date = models.DateTimeField(blank = True,null = True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    costcenter = models.ForeignKey(Costcenter,on_delete=models.CASCADE,null=True,blank=True)
    is_group = models.CharField(max_length=1)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pincode = models.CharField(max_length=20)
    entry_date = models.DateTimeField(blank = True,null = True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Relationship(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class GST_category(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Customer_Supplier(models.Model):
    salutation = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    type_of = models.CharField(max_length=200)
    relation_ship = models.ForeignKey(Relationship,on_delete=models.CASCADE,null=True,blank=True)
    GST_category = models.ForeignKey(GST_category,on_delete=models.CASCADE,null=True,blank=True)
    pan = models.CharField(max_length=40)
    GSTIN = models.CharField(max_length=50)
    entry_date = models.DateTimeField(blank = True,null = True)
    commission_rate = models.CharField(max_length=50)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Address(models.Model):
    link_name = models.CharField(max_length=200)
    Line_1 = models.CharField(max_length=200)
    Line_2 = models.CharField(max_length=200)
    Line_3 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    type_of = models.CharField(max_length=200)
    address_type_of = models.CharField(max_length=200)
    entry_date = models.DateTimeField(blank = True,null = True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    link_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    telephone= models.CharField(max_length=200)
    email= models.EmailField()
    type_of_details = models.CharField(max_length=200)
    aadhaar = models.CharField(max_length=200)
    voter_id = models.CharField(max_length=200)
    driving_licence = models.CharField(max_length=200)
    pan = models.CharField(max_length=200)
    type_of = models.CharField(max_length=200)
    entry_date = models.DateTimeField(blank = True,null = True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Item_type(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Tax_type(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Tax(models.Model):
    name = models.CharField(max_length=200)
    rate = models.CharField(max_length=200)
    tax_type = models.ForeignKey(Tax_type,on_delete=models.CASCADE,null=True,blank=True)
    cost_center = models.ForeignKey(Costcenter,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Warranty_type(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Warranty(models.Model):
    name = models.CharField(max_length=200)
    warrenty_type = models.ForeignKey(Warranty_type,on_delete=models.CASCADE,null=True,blank=True)
    duration = models.IntegerField()
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    UOM = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    serial_no = models.CharField(max_length=200)
    batch_no = models.CharField(max_length=200)
    item_type = models.ForeignKey(Item_type,on_delete=models.CASCADE,null=True,blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    barcode = models.CharField(max_length=200)
    tax = models.ForeignKey(Tax,on_delete=models.CASCADE,null=True,blank=True)
    HSN_SAC = models.CharField(max_length=200,null=True)
    model_no = models.CharField(max_length=200,null=True)
    warranty = models.ForeignKey(Warranty,on_delete=models.CASCADE,null=True,blank=True)
    start_warranty = models.DateTimeField(blank = True,null = True)
    end_warrenty = models.DateTimeField(blank = True,null = True)
    entry_date = models.DateTimeField(blank = True,null = True)
    is_salable = models.BooleanField(default=False)
    is_purchase = models.BooleanField(default=False)
    is_stock = models.BooleanField(default=False)
    is_fixed_asset = models.BooleanField(default=False)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Liability(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Income(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Equity(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Account_nature(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Account_type(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Balance_type(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Frozen(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Root_type(models.Model):
    name = models.CharField(max_length=500)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Is_group(models.Model):
    name = models.CharField(max_length=50)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Root_account_type(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Account(models.Model):
    account_name = models.CharField(max_length=500)
    account_number = models.CharField(max_length=200)
    is_group = models.ForeignKey(Is_group,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    costcenter = models.ForeignKey(Costcenter,on_delete=models.CASCADE,null=True,blank=True)
    root_type = models.ForeignKey(Root_type,on_delete=models.CASCADE,null=True,blank=True)
    account_nature = models.ForeignKey(Account_nature,on_delete=models.CASCADE,null=True,blank=True)
    account_type=models.ForeignKey(Account_type,on_delete=models.CASCADE,null=True,blank=True)
    root_account_type= models.ForeignKey(Root_account_type,on_delete=models.CASCADE,null=True,blank=True)
    balance_type = models.ForeignKey(Balance_type,on_delete=models.CASCADE,null=True,blank=True)
    rate=models.CharField(max_length=200)
    frozen=models.ForeignKey(Frozen,on_delete=models.CASCADE,null=True,blank=True)
    entry_date = models.DateTimeField(blank = True,null = True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.account_name

class Parent_account(models.Model):
    name = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Discount_on(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Discount_type(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Item_discount(models.Model):
    discount_on = models.ForeignKey(Discount_on,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    discount_rate = models.CharField(max_length=200)
    discount_type = models.ForeignKey(Discount_type,on_delete=models.CASCADE,null=True,blank=True)
    price = models.CharField(max_length=200)
    qty = models.CharField(max_length=200)
    entry_date = models.DateTimeField(blank = True,null = True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Item_rate_type(models.Model):
    name = models.CharField(max_length=200)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Item_valuation_rate(models.Model):
    code = models.ForeignKey(Item,on_delete=models.CASCADE,null=True,blank=True)
    rate = models.CharField(max_length=200)
    item_rate_type = models.ForeignKey(Item_rate_type,on_delete=models.CASCADE, null=True, blank=True)
    warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE,null=True,blank=True)
    entry_date = models.DateTimeField(blank = True,null = True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    docstatus = models.BooleanField(default=True)
    disable = models.BooleanField(default=False)


    def __str__(self):
        return self.name



class Manage_Device_Details(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    computer_info = models.CharField(max_length=200)
    location_details = models.CharField(max_length=200)
    mac_address = models.CharField(max_length=200)
    cpu_desc = models.CharField(max_length=200)
    motherboard_desc = models.CharField(max_length=200)
    hdd_desc = models.CharField(max_length=200)
    ram_desc = models.CharField(max_length=200)
    monitor_desc = models.CharField(max_length=200)
    other_desc = models.TextField()
    username = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    #operating_system = models.ForeignKey(OS,on_delete=models.CASCADE,null=True,blank=True)





