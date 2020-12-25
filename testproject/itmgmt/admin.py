from django.contrib import admin

# Register your models here.
from .models import *

class Post_Admin(admin.ModelAdmin):
    model=Post
    list_display = ["title","id","on_date"]

admin.site.register(Post,Post_Admin)
admin.site.register(Post_Type)
admin.site.register(Docstatus)

class User_Detail(admin.ModelAdmin):
    model=User
    list_display = ['login','password','name','email','mobile','department']
admin.site.register(Department)
admin.site.register(User,User_Detail)

class Company_Detail(admin.ModelAdmin):
    model=Company
    list_display = ['name','address','city','district','state','country','pincode','gstin','docstatus','disable']
admin.site.register(Company,Company_Detail)

class Costcenter_Detail(admin.ModelAdmin):
    model=Costcenter
    list_display = ['name','address','city','district','state','country','pincode','gstin','docstatus','disable','company']
admin.site.register(Costcenter,Costcenter_Detail)

class Warehouse_Detail(admin.ModelAdmin):
    model=Warehouse
    list_display = ['name','company','costcenter','is_group','address','city','district','state','country','pincode','docstatus','disable']
admin.site.register(Warehouse,Warehouse_Detail)

admin.site.register(Relationship)

admin.site.register(GST_category)

class Customer_supplier_Detail(admin.ModelAdmin):
    model=Customer_Supplier
    list_display = ['salutation','name','gender','type_of','relation_ship','GST_category','pan','GSTIN','commission_rate','docstatus','disable']
admin.site.register(Customer_Supplier,Customer_supplier_Detail)


class Address_Detail(admin.ModelAdmin):
    model=Address
    list_display = ['link_name','Line_1','Line_2','Line_3','city','district','state','country','pincode','type_of','address_type_of','docstatus','disable']
admin.site.register(Address,Address_Detail)

class Contact_Detail(admin.ModelAdmin):
    model=Contact
    list_display=['link_name','mobile','telephone','email','type_of_details','aadhaar','voter_id','driving_licence','pan','type_of','docstatus','disable']
admin.site.register(Contact,Contact_Detail)

admin.site.register(Brand)
admin.site.register(Item_type)
admin.site.register(Tax_type)

class Tax_Details(admin.ModelAdmin):
    model=Tax
    list_display=['name','rate','tax_type','cost_center','company','docstatus','disable']
admin.site.register(Tax,Tax_Details)

class Warranty_type_Details(admin.ModelAdmin):
    model=Warranty_type
    list_display=['name','docstatus','disable']
admin.site.register(Warranty_type,Warranty_type_Details)

class Warranty_Details(admin.ModelAdmin):
    model=Warranty
    list_display=['name','warrenty_type','duration','docstatus','disable']
admin.site.register(Warranty,Warranty_Details)

class Item_Details(admin.ModelAdmin):
    model=Item
    list_display=['name','code','UOM','description','serial_no','batch_no','item_type','brand','barcode','tax','HSN_SAC','model_no','warranty','start_warranty','end_warrenty','entry_date','is_salable','is_purchase','is_stock','is_fixed_asset','docstatus','disable']
admin.site.register(Item,Item_Details)

class Asset_Details(admin.ModelAdmin):
    model=Asset
    list_display=['name','docstatus','disable']
admin.site.register(Asset,Asset_Details)

class Liability_Details(admin.ModelAdmin):
    model=Liability
    list_display=['name','docstatus','disable']
admin.site.register(Liability,Liability_Details)

class Income_Details(admin.ModelAdmin):
    model=Income
    list_display=['name','docstatus','disable']
admin.site.register(Income,Income_Details)

class Expense_Details(admin.ModelAdmin):
    model=Expense
    list_display=['name','docstatus','disable']
admin.site.register(Expense,Expense_Details)

class Equity_Details(admin.ModelAdmin):
    model=Equity
    list_display=['name','docstatus','disable']
admin.site.register(Equity,Equity_Details)

class Account_nature_Details(admin.ModelAdmin):
    model=Account_nature
    list_display=['name','docstatus','disable']
admin.site.register(Account_nature,Account_nature_Details)

class Account_type_details(admin.ModelAdmin):
    model=Account_type
    list_display=['name','docstatus','disable']
admin.site.register(Account_type,Account_type_details)

class Balance_type_Details(admin.ModelAdmin):
    model=Balance_type
    list_display=['name','docstatus','disable']
admin.site.register(Balance_type,Balance_type_Details)

class Frozen_Details(admin.ModelAdmin):
    model=Frozen
    list_display=['name','docstatus','disable']
admin.site.register(Frozen,Frozen_Details)

class Root_type_Details(admin.ModelAdmin):
    model=Root_type
    list_display=['name','docstatus','disable']
admin.site.register(Root_type,Root_type_Details)

class Is_group_details(admin.ModelAdmin):
    model=Is_group
    list_display=['name','docstatus','disable']
admin.site.register(Is_group,Is_group_details)

class Root_account_type_Details(admin.ModelAdmin):
    model=Root_account_type
    list_display=['name','docstatus','disable']
admin.site.register(Root_account_type,Root_account_type_Details)

class Account_Details(admin.ModelAdmin):
    model=Account
    list_disaplay=['account_name','account_number','is_group','company','costcenter','root_type','account_nature','account_type','root_account_type','balance_type','rate']
admin.site.register(Account,Account_Details)

class Parent_account_Details(admin.ModelAdmin):
    model=Parent_account
    list_display=['name','docstatus','disable']
admin.site.register(Parent_account,Parent_account_Details)

class Discount_on_Details(admin.ModelAdmin):
    model = Discount_on
    list_display=['name','docstatus','disable']
admin.site.register(Discount_on,Discount_on_Details)

class Discount_type_Details(admin.ModelAdmin):
    model = Discount_type
    list_display=['name','docstatus','disable']
admin.site.register(Discount_type,Discount_type_Details)

class Discount_apply_on_Details(admin.ModelAdmin):
    model = Discount_apply_on
    list_display=['name','docstatus','disable']
admin.site.register(Discount_apply_on,Discount_apply_on_Details)

class Discount_value_type_Details(admin.ModelAdmin):
    model = Discount_value_type
    list_display=['name','docstatus','disable']
admin.site.register(Discount_value_type,Discount_value_type_Details)

class Item_discount_Details(admin.ModelAdmin):
    model = Item_discount
    list_display=['discount_on','name','discount_rate','discount_type','min_price','max_price','min_qty','max_qty','company','costcenter','warehouse']
admin.site.register(Item_discount,Item_discount_Details)

class Item_rate_type_Details(admin.ModelAdmin):
    model = Item_rate_type
    list_display=['name','docstatus','disable']
admin.site.register(Item_rate_type,Item_rate_type_Details)

class Item_valuation_rate_Details(admin.ModelAdmin):
    model = Item_valuation_rate
    list_display=['code','rate','item_rate_type','warehouse','entry_date','docstatus','disable']
admin.site.register(Item_valuation_rate,Item_valuation_rate_Details)



