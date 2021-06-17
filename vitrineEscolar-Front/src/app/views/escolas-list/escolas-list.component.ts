import { Component, OnInit } from '@angular/core';
import { observable, Observable } from 'rxjs';
import { SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-escolas-list',
  templateUrl: './escolas-list.component.html',
  styleUrls: ['./escolas-list.component.css']
})
export class EscolasListComponent implements OnInit {

  constructor(private service:SharedService) { }

  EscolaList:any=[];
  EscolaActiveCarrousel:any;

  ngOnInit(): void {
    this.refreshDepList();
  }

  refreshDepList() {
    this.service.getEscolaList().subscribe(data=>{
      this.EscolaList=data;
      this.EscolaActiveCarrousel = this.EscolaList?.results[0];
    });
  }

  detail(dataItem: any): void {
    this.service.selectedSchool = dataItem;
  }
}
